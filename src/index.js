import getInfo from "./get-info.js";
import getRelease from "./get-release.js";
import getSpec from "./get-spec.js";

let name = process.argv[2];

getInfo(name)
    .then(getRelease)
    .then(rel => {
        getSpec(name).then(spec => {
            spec.set("Version", rel.slice(1));

            console.log(spec.toString());
        });
    })
    .catch(err => console.log("An error occured", err));
