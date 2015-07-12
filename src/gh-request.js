import https from "https";

export default function(path) {
    return new Promise((resolve, reject) => {
        https.get({
            host: "api.github.com",
            path: path,
            headers: { "user-agent": "node" }
        }, function(res) {
            let body = "";

            res.on("data", function(chunk) {
                body += chunk;
            });

            res.on("end", function() {
                resolve(JSON.parse(body));
            });
        }).on("error", reject);
    });
}
