from mw2fcitx.tweaks.moegirl import tweaks

exports = {
    "source": {
        "api_path": "https://dontstarve.huijiwiki.com/api.php",
        "file_path": [],
        "kwargs": {
            "output": "dontstarve_titles.txt"
        }
    },
    "tweaks":
        tweaks,
    "converter": {
        "use": "opencc",
        "kwargs": {}
    },
    "generator": [{
        "use": "rime",
        "kwargs": {
            "output": "dontstarve.dict.yaml"
        }
    }, {
        "use": "pinyin",
        "kwargs": {
            "output": "dontstarve.dict"
        }
    }]
}
