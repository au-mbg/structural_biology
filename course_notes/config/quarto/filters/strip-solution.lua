function Div(div)
  local ex = div.attributes["solution"]
  if ex ~= nil and string.lower(ex) == "true" then
    return {}
  end
  return nil
end
