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

## Assets  
Assets can be anything ranging from textures, to meshes and shaders. 
If an asset is modified, the file will be hot-reloaded while the app keeps running. 
It is also easy to register custom asset classes with the content manager by registering a file path suffix with an associated loader function.   

## Scripts
The **MainScript** class supports entrypoints for game applications through **vvs_init**, **vvs_update**, **vvs_draw** and **vvs_exit**.
These functions will be called by the ververser host at the right moments in the game loop.

While you can use regular import statements in your scripts, their content will not be hot-reloaded. 
This is where we encounter some issues.
There are a few issues when trying to reload modules in Python. 
Python does not allow us to easily and completely unload modules, 
and uses an internal cache to prevent reloads of modules that have been loaded before. 
When we have modified a module, these mechanisms prevent us from properly reloading the modified code. 

To bypass Python's internal importing mechanisms, 
we use a generic **Script** class that can be used to encapsulate arbitrary python code, 
and hides it from Pythons internal import mechanisms.
To import Script instances and register them with the content manager, 
you can use the **import_script** function, instead of the normal import statement. 

Finally, there is the question of what exactly needs to be reloaded when a script is modified. 
Currently, when a single script is modified, the entire app logic is reinitialised starting from the main script.
This is often fine for smaller creative coding projects. 
If you want to preserve some state, 
you could also consider writing state to file in vvs_exit, and reading it back in, in vvs_init. 
Note that there is no way to recover from errors in vvs_exit, 
as the code can not be hot-reloaded while keeping state, 
if your custom mechanism that is responsible for preserving state, is the thing that crashes...
So, in that case, the app is simply reloaded, and you will lose your state.
Finally, you could also tag some scripts with a custom suffix, and register them as Assets! 
This way, only the scripts itself will be reloaded, and not the entire app. 
This is especially useful for python modules that contain only functions and keep no state. 


## Examples

Ververser comes with a few examples that can be found in _ververser/examples_.  
Every example comes with its own readme, explaining things from a minimal setup, 
to how scripts can be imported in such a way that they will be properly reloaded on changes.
