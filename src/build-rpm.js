import getInfo from "./get-info.js";
import getSpec from "./get-spec.js";
import ghRequest from "./gh-request.js";
import extractRepoInfo from "./extract-repo-info.js";

export default function(name) {
    getInfo(name)
        .then(info => {
            let git = extractRepoInfo(info.repository.url);

            return Promise.all([
                ghRequest("/repos/" + git.org + "/" + git.repo),
                ghRequest("/repos/" + git.org + "/" + git.repo + "/releases")
            ]);
        })
        .then(data => {
            return getSpec(name).then(spec => {
                spec.set("Version", data[1][0].tag_name.slice(1));
                spec.set("%description", data[0].description + "\n\n");

                console.log(spec.toString());
            });
        })
        .catch(err => console.log("An error occured", err));
}
