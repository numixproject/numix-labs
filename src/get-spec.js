import fs from "fs";
import Spec from "./spec.js";

export default function(name) {
    return new Promise((resolve, reject) => {
        fs.readFile(__dirname + "/../data/" + name + ".spec", (err, data) => {
            if (err) {
                reject(err);
            } else {
                let spec = new Spec(data.toString());

                resolve(spec);
            }
        });
    });
}
