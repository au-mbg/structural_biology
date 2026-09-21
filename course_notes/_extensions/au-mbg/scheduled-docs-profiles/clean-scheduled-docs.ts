
import { existsSync } from "https://deno.land/std/fs/mod.ts";
import { readConfig, readScheduledDocs, removeTempDir } from "./scheduled-docs.ts";

const configParams = await readConfig();
const ymlPath = configParams['path-to-yaml']

// Clean up the placeholder created when no applicable schedule exists.
if (!existsSync(ymlPath)) {
    // Clean up the placeholder draft-list.yml we might have created
    if (existsSync("scheduled-docs_files/draft-list.yml")) {
        try {
            const content = Deno.readTextFileSync("scheduled-docs_files/draft-list.yml");
            if (content.startsWith("# Scheduling disabled or no _schedule.yml found")) {
                Deno.removeSync("scheduled-docs_files/draft-list.yml");
                // Also remove directory if empty
                try {
                    Deno.removeSync("scheduled-docs_files");
                } catch {
                    // Directory not empty or doesn't exist, that's fine
                }
            }
        } catch {
            // File doesn't exist or can't read, that's fine
        }
    }
    Deno.exit(0);
}

const scheduledDocsKey = configParams['scheduled-docs-key'];
const tempFilesDir = configParams['temp-files-dir'];

// Run functions
const scheduledDocs = await readScheduledDocs(ymlPath, scheduledDocsKey, configParams);
await removeTempDir(scheduledDocs, tempFilesDir);
