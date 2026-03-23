function Div(div)
  local ex = div.attributes["exercise"]
  if ex ~= nil and string.lower(ex) == "true" then
    return {}
  end
  return nil
end
