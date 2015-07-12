import extractRepoInfo from "./extract-repo-info.js";
import ghRequest from "./gh-request.js";

export default function(info) {
    let git = extractRepoInfo(info.repository.url);

    return new Promise((resolve, reject) => {
        ghRequest("/repos/" + git.org + "/" + git.repo + "/releases").then(data => {
            resolve(data[0].tag_name);
        }).catch(reject);
    });
}
