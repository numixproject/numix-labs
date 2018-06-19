import getSpec from "./get-spec.js";
import ghRequest from "./gh-request.js";
import extractRepoInfo from "./extract-repo-info.js";

export default function(name) {
    getSpec(name)
        .then(spec => {
            let git = extractRepoInfo(spec.get("URL"));

            return ghRequest("/repos/" + git.org + "/" + git.repo + "/releases").then(data => {
                spec.set("Version", data[0].tag_name.slice(1));

                console.log(spec.toString());
            });
        })
        .catch(err => console.log("An error occured", err));
}
