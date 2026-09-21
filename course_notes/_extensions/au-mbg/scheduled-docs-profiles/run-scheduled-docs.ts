
import { existsSync } from "https://deno.land/std/fs/mod.ts";
import { ensureDirSync } from "https://deno.land/std/fs/mod.ts";

// Import external libraries
import { readConfig, readScheduledDocs, propagateKeys, setDraftStatuses, writeDraftList, writeSchedule, writeListingContents, writeAutonavContents } from "./scheduled-docs.ts";

console.log("=== Scheduled-docs ===");

// Get parameters
const configParams = await readConfig();
const ymlPath = configParams['path-to-yaml']
const scheduledDocsKey = configParams['scheduled-docs-key'];
const itemsKey = configParams['docs-key'];
const tempFilesDir = configParams['temp-files-dir'];

// Silently skip projects that do not define either a profile schedule or the
// configured base schedule. The placeholder satisfies metadata-files.
if (!existsSync(ymlPath)) {
    ensureDirSync(tempFilesDir);
    Deno.writeTextFileSync(
        `${tempFilesDir}/draft-list.yml`,
        "# Scheduling disabled or no _schedule.yml found\nwebsite:\n  drafts: []\n",
    );
    Deno.exit(0);
}

let dateFormat = configParams['date-format'];
if ( dateFormat === undefined ) {
    dateFormat = "yyyy-MM-dd";
}

// Run functions
let scheduledDocs = await readScheduledDocs(ymlPath, scheduledDocsKey, configParams);
propagateKeys(scheduledDocs);
setDraftStatuses(scheduledDocs, itemsKey, dateFormat, ymlPath);
await writeDraftList(scheduledDocs, tempFilesDir);
await writeSchedule(scheduledDocs, tempFilesDir);
await writeListingContents(scheduledDocs, tempFilesDir);
await writeAutonavContents(scheduledDocs, tempFilesDir);
