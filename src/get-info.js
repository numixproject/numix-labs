import fs from "fs";

export default function(name) {
    return new Promise((resolve, reject) => {
        fs.readFile(__dirname + "/../data/" + name + ".json", function(err, data) {
            if (err) {
                reject(err);
            } else {
                let parsed = JSON.parse(data.toString());

                resolve(parsed);
            }
        });
    });
}
