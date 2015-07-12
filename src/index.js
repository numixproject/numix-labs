import getInfo from "./get-info.js";
import getRelease from "./get-release.js";

let name = process.argv[2];

getInfo(name)
    .then(getRelease)
    .then(rel => console.log(`Latest release is ${rel}`))
    .catch(err => console.log("An error occured", err));
