# config-diff-tool

Diff two configuration files while ignoring blank lines and `#` / `;`
comment lines, so a comment-only edit shows as no change.

## How to run

```bash
python3 main.py old.conf new.conf
```

## Example output

```text
Added: 1, Removed: 1
--- 
+++ 
@@ -1,2 +1,2 @@
 a=1
-b=2
+c=3
```

Standard library only. No network access.
