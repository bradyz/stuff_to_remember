# Stuff I always google

## Ubuntu Screenshot

* Copy window to clipboard `ctrl+alt+printscreen``
* Copy selection to clipboard `ctrl+shift+printscreen`

## tar with progress bar

```
function tarc {
    tar czf - $1 -P | pv -s $(du -sb $1 | cut -f 1) > $1.tar.gz
}
```

```
function tarx {
    pv $1 | tar -xz
}
```

## rsync

```
rsync -avz --info=progress2 $SRC $DST
```

## Chrome

* Delete from suggestion bar `ctrl+shift+delete`

## VSCode `launch.json`

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "cwd": "/PATH/TO/WORK_DIR",
            "justMyCode": false,
            "env": {
                "FOO": "BAR",
            },
            "args": [
                 "foo", "bar",
            ]
        }
    ]
}
```

## SSH and tmux

```
ssh -XC USER@hHOST -t 'tmux new-session -A -s TMUX_ID'
```

## Conda

```
conda create --name NAME python=3.9

conda env create --name NAME --file=environments.yml

conda env export --no-builds | grep -v "prefix" > environment.yml
conda env export --name NAME --no-builds | grep -v "prefix" > environment.yml

conda env update --file environment.yml --prune
conda env update --name NAME --file environment.yml --prune
```

## Soft Links

```
ln -s SRC DST
```
