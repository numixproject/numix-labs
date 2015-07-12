/**
 * Supported URL formats:
 *
 * - https://github.com/org/repo
 * - https://github.com/org/repo.git
 * - git@github.com:org/repo.git
 * - git+https://github.com/org/repo.git"
 */

export default function(url) {
    let parts = url.replace(/^((git@|.+\/\/)([^:^\/]+)(\/|:))/, "").replace(/\.git$/, "").split("/");

    return {
        org: parts[0],
        repo: parts[1]
    };
}
