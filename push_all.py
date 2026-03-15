"""
Pushes all 23 site files directly to GitHub via API.
Run: python3 push_all.py
"""
import os, base64, urllib.request, urllib.error, json, time

TOKEN      = "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"
REPO_OWNER = "tpruitt-ss"
REPO_NAME  = "southern-software"
BRANCH     = "main"

API     = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents"
HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json",
    "Content-Type": "application/json",
    "X-GitHub-Api-Version": "2022-11-28",
}

def api(path, method="GET", data=None):
    url  = f"{API}/{path}"
    body = json.dumps(data).encode() if data else None
    req  = urllib.request.Request(url, data=body, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read()), r.status
    except urllib.error.HTTPError as e:
        return json.loads(e.read()), e.code

def get_sha(filename):
    res, status = api(filename)
    return res.get("sha") if status == 200 else None

def push(local_path, repo_filename):
    with open(local_path, "rb") as f:
        content = base64.b64encode(f.read()).decode()
    sha     = get_sha(repo_filename)
    payload = {"message": f"Update {repo_filename}", "content": content, "branch": BRANCH}
    if sha:
        payload["sha"] = sha
    res, status = api(repo_filename, method="PUT", data=payload)
    ok = status in (200, 201)
    print(f"  {'✓' if ok else '✗'} {'Updated' if sha else 'Created'}: {repo_filename}" +
          (f"  ← ERROR: {res.get('message','')}" if not ok else ""))
    return ok

def push_nojekyll():
    sha     = get_sha(".nojekyll")
    payload = {"message": "Add .nojekyll", "content": base64.b64encode(b"").decode(), "branch": BRANCH}
    if sha:
        payload["sha"] = sha
    res, status = api(".nojekyll", method="PUT", data=payload)
    print(f"  {'✓' if status in (200,201) else '✗'} .nojekyll")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    html_files = sorted(f for f in os.listdir(script_dir) if f.endswith(".html"))
    img_files  = sorted(f for f in os.listdir(script_dir) if f.endswith("-trans.png"))

    print(f"\nPushing {len(html_files)} HTML + {len(img_files)} images to {REPO_OWNER}/{REPO_NAME}...\n")

    push_nojekyll()

    print("\n── Images ──────────────────────")
    for f in img_files:
        push(os.path.join(script_dir, f), f)
        time.sleep(0.3)

    print("\n── HTML Pages ──────────────────")
    for f in html_files:
        push(os.path.join(script_dir, f), f)
        time.sleep(0.3)

    print(f"\n✅ Done! Wait 60 seconds then visit:")
    print(f"   https://{REPO_OWNER}.github.io/{REPO_NAME}/\n")
