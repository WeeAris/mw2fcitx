from mw2fcitx.tweaks.moegirl import tweaks

exports = {
    "source": {
        "api_path": "https://libraryofruina.huijiwiki.com/api.php",
        "file_path": [],
        "kwargs": {
            "output": "libraryofruina_titles.txt"
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
            "output": "libraryofruina.dict.yaml"
        }
    }, {
        "use": "pinyin",
        "kwargs": {
            "output": "libraryofruina.dict"
        }
    }]
}
