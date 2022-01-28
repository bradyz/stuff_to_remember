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
