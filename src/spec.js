const sections = [ "prep", "build", "install", "clean", "pre", "post", "preun", "postun", "files", "changelog" ];

class Spec {
    constructor(content) {
        if (typeof content !== "string") {
            throw new Error("Content must be string");
        }

        this._data = [];

        let lines = content.toString().split("\n");

        for (let line of lines) {
            let matched = line.match(/(^[A-Z][a-zA-Z]+)(:\s*)(.+)/);

            if (Array.isArray(matched)) {
                this._data.push({
                    key: matched[1],
                    value: matched[3],
                    separator: matched[2],
                    type: "property"
                });
            } else {
                if (line.indexOf("%") === 0 && sections.indexOf(line.slice(1)) > -1) {
                    this._data.push({
                        key: line,
                        value: "",
                        separator: "\n",
                        type: "section"
                    });

                    continue;
                }

                let last = this._data[this._data.length - 1];

                if (last && last.type === "section") {
                    last.value += "\n" + line;
                } else {
                    this._data.push({
                        value: line,
                        type: "raw"
                    });
                }
            }
        }
    }

    get(key) {
        for (let item of this._data) {
            if (item && item.key === key) {
                return item.value;
            }
        }
    }

    set(key, value) {
        for (let item of this._data) {
            if (item && item.key === key) {
                item.value = value;

                break;
            }
        }
    }

    toString() {
        let raw = "";

        for (let item of this._data) {
            if (item.type === "raw") {
                raw += item.value;
            } else {
                raw += item.key + item.separator + item.value;
            }

            raw += "\n";
        }

        return raw;
    }
}

export default Spec;
