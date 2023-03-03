# Ververser

**Ververser is a lightweight wrapper around pyglet that allows hot-reloading of content.** 

When your app is running, changes to content will automatically be hot-reloaded.
If an error occurs, the app is automatically paused, 
and will automatically be resumed when content is updated. 
All you need to do is save your changes. 
This makes the development workflow faster as you do not have to restart the entire app every time an asset is changed. 
This is especially useful for creative coding. 

Ververser makes a distinction between two types of content:

- **Scripts**  
The _MainScript_ class supports entrypoints for game applications through _vvs_init_, _vvs_update_, and _vvs_draw_.
The generic _Script_ class can be used to encapsulate arbitrary python code. 
Scripts can import other scripts. 
This can make dependency-management and object lifetime management during hot-reloading difficult, 
so to keep things simple; if just a single script is modified, all scripts will be hot-reloaded.


- **Assets**  
Assets can be anything ranging from textures, to meshes and shaders. 
If an asset is modified, the file will be hot-reloaded, but this will not necessarily affect any logic from scripts, 
and the app will just continue running normally. 
It is also easy to register custom asset classes with the content manager.


## Examples

Ververser comes with a few examples that can be found in _ververser/examples_.  
Every example comes with its own readme, explaining things from a minimal setup, 
to how scripts can be imported in such a way that they will be properly reloaded on changes.

## Install 

Ververser is available via PyPI:

```
pip install ververser
```