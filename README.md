# Ververser

**Ververser is a lightweight wrapper around pyglet that allows hot-reloading of content.** 

When your app is running, changes to content will automatically be hot-reloaded.
If an error occurs, the app is automatically paused, 
and will automatically be resumed when content is updated. 
All you need to do is save your changes. 
This makes the development workflow faster as you do not have to restart the entire app every time an asset is changed. 
This is especially useful for creative coding. 

Ververser is available via PyPI:

```
pip install ververser
```

## Examples
Curious what working with ververser looks like?

Ververser comes with a few examples that can be found in _ververser/examples_. 
Every example comes with its own readme, explaining things from a minimal setup, 
to how scripts can be imported in such a way that they will be properly reloaded on changes. 
Just run an example, and start changing the code of the example, while running, to see how content will be reloaded. 

Another example of what can be achieved with ververser is [**speelgrond**](https://github.com/berryvansomeren/speelgrond)

## Assets  
Assets can be anything ranging from textures, to meshes and shaders. 
If an asset is modified, the file will be hot-reloaded while the app keeps running. 
It is also easy to register custom asset classes with the content manager by registering a file path suffix 
with an associated custom loader function. 
Note that asset loaders that are registered later, overrule earlier registered ones.

## Scripts
Ververser supports two ways of defining entrypoints for your application. 
These entrypoints will be called by the ververser host at the right moments in the game loop.
You could define a **main.py** file with hooks for game applications through **vvs_init**, **vvs_update**, **vvs_draw** and **vvs_exit**.
Instead of defining these hooks as free functions, one could also choose to define a **VVSGame** class in a **game.py** file, 
which will be instantiated, managed and invoked by ververser. 
In this case your class can implement vvs_update, vvs_draw and vvs_exit. 
However, in this case there is no vvs_init hook, as the class's initializer fulfills that role instead. 

### Why we bypass Python's internal import mechanics
There are a few issues when trying to reload modules in Python. 
Python does not allow us to easily and completely unload modules, 
and uses an internal cache to prevent reloads of modules that have been loaded before. 
When we modify a module, these mechanisms prevent us from properly reloading the modified code. 

### How to import ververser scripts
To bypass Python's internal importing mechanisms, 
we use a generic **Script** class that can be used to encapsulate arbitrary python code, 
and hides it from Pythons internal import mechanisms.
To import Script instances and register them with the content manager, 
you can use the **import_script** function, instead of the normal import statement. 

### Script reloads
One particularly confusing issue can arise when one script contains instances of objects,
whose definition is in another script.
When the object definition is changed, what do we expect to happen to the already existing instances,
and how do we keep track of the dependencies?

By default, ververser reinitialises all scripts, when just one of them is modified. 
This is the easiest to manage, leads to the least confusion, and is often fine for smaller creative coding projects. 
If you do want to take control over managing this issue yourself, 
it is as simple as passing **reinit_on_mod = False** to **import_script**.
The script will still be watched and hot-reloaded when modifications are made, 
but the script will not be grouped with scripts that would trigger full reinitialisation,
and you will not be protected against the issues mentioned above.
Internally, ververser will then actually consider the script to be an Asset!
This is great for example for modules that do not directly contribute to any particular state of your application.

Note that you should not try to create references to functions of modules imported this way with _reinit_on_mod = False_.
This is exactly because of the issues mentioned above; 
the reference will not be updated when the module with the function definition is updated.
However, referencing through the Script class does work, 
because the Script class will retrieve the definition anew, for every "get".

Finally, note that if you do not want to hot-reload a module at all, 
you can of course still use normal python imports.

### Preserving state
If you want to preserve some state between reloads, 
you could consider writing state to file in vvs_exit, and reading it back in, in vvs_init. 
By managing script reloads as described in the previous section you can also minimize the amount of lost state.

### Some closing remarks on exit errors
Note that there is no way to recover from errors in vvs_exit, 
as the code can not be hot-reloaded while keeping state, 
if your custom mechanism that is responsible for preserving state, is the thing that crashes...
So, in that case, the app is simply reloaded, and you will lose your state.
Also note that when you feel you might have fixed your issue in the vvs_exit call, 
the error might still be logged, because on reload, the previously defined version of vvs_exit is called, 
as your new code is not loaded yet (but will be on the next game "tick"). 
