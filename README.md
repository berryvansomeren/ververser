# Ververser

**Ververser is a lightweight wrapper around pyglet that allows hot-reloading of assets.** 

The only default asset class known by ververser is the Python script, 
but it is easy to register custom asset classes.
When your app is running, changes to assets will automatically be hot-reloaded.
If an error occurs, the app is automatically paused, 
and will automatically be resumed when assets are updated. 
All you need to do is save your changes. 

This makes the development workflow faster as you do not have to restart the entire app every time an asset is changed. 

## Install 

Ververser is available via PyPI:

```
pip install ververser
```