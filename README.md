# Ververser

**Ververser is a lightweight wrapper around pyglet that allows hot-reloading of assets.** 

The only default asset class known by ververser is the Python game script, 
which supports _init_, _update_ and _draw_ functions. 
However, it is easy to register custom asset classes with the asset manager.
When your app is running, changes to assets will automatically be hot-reloaded.
If an error occurs, the app is automatically paused, 
and will automatically be resumed when assets are updated. 
All you need to do is save your changes. 

This makes the development workflow faster as you do not have to restart the entire app every time an asset is changed. 
This is especially useful for creative coding. 

## Examples

Vervser comes with a few examples. Please see _ververser/examples_.  
Every example comes with its own readme, explaining things from a minimal setup, 
to how scripts can be imported in such a way that they will be properly reloaded on changes.

## Install 

Ververser is available via PyPI:

```
pip install ververser
```