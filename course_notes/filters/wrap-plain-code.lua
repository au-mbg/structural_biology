-- For plain (unlabelled) or `pymol`-tagged code blocks in HTML output, emit
-- HTML that exactly matches Pandoc's highlighted structure (including per-line
-- span IDs and anchor elements) so all CSS rules and sizing are identical.
local plain_languages = { [""] = true, ["pymol"] = true }
local block_counter = 0

function CodeBlock(block)
  if FORMAT ~= "html" then return nil end
  local lang = block.classes[1] or ""
  if not plain_languages[lang] then return nil end

  block_counter = block_counter + 1
  local cb = "cb" .. block_counter

  local text = block.text:gsub("\n$", "")
    :gsub("&", "&amp;"):gsub("<", "&lt;"):gsub(">", "&gt;")
  local spans = {}
  local n = 0
  for line in (text .. "\n"):gmatch("([^\n]*)\n") do
    n = n + 1
    local sid = cb .. "-" .. n
    table.insert(spans,
      '<span id="' .. sid .. '">' ..
      '<a href="#' .. sid .. '" aria-hidden="true" tabindex="-1"></a>' ..
      line .. '</span>')
  end
  return pandoc.RawBlock("html",
    '<div class="sourceCode" id="' .. cb .. '">' ..
    '<pre class="sourceCode pymol"><code class="sourceCode pymol">' ..
    table.concat(spans, "\n") ..
    "</code></pre></div>")
end
