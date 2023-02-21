from mw2fcitx.tweaks.moegirl import tweaks

exports = {
    "source": {
        "api_path": "https://taiwu.huijiwiki.com/api.php",
        "file_path": [],
        "kwargs": {
            "output": "taiwu_titles.txt"
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
            "output": "taiwu.dict.yaml"
        }
    }, {
        "use": "pinyin",
        "kwargs": {
            "output": "taiwu.dict"
        }
    }]
}
