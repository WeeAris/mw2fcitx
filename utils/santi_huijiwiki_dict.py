from mw2fcitx.tweaks.moegirl import tweaks

exports = {
    "source": {
        "api_path": "https://santi.huijiwiki.com/api.php",
        "file_path": [],
        "kwargs": {
            "output": "santi_titles.txt"
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
            "output": "santi.dict.yaml"
        }
    }, {
        "use": "pinyin",
        "kwargs": {
            "output": "santi.dict"
        }
    }]
}
