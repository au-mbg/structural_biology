local collapse_by_default = {
  tip = true,
}

function Callout(callout)
  if collapse_by_default[callout.type] and callout.collapse == nil then
    callout.collapse = true
  end
  return callout
end