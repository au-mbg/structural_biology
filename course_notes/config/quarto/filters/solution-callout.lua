local function has_class(div, class)
  for _, c in ipairs(div.classes or {}) do
    if c == class then return true end
  end
  return false
end

return {
  Div = function(div)
    if not has_class(div, "solution-callout") then
      return nil
    end

    -- Strip entirely when not in instructor profile
    local profile = os.getenv("QUARTO_PROFILE") or ""
    if not profile:find("solution") then
      return {}
    end

    local title = div.attributes["title"] or "Svar"

    -- Render as a proper Quarto callout for the instructor
    return quarto.Callout({
      type = "important",
      title = title,
      collapse = true,
      content = div.content,
    })
  end
}