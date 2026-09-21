export type PathExists = (path: string) => boolean;

export function parseProfiles(profileValue: string | undefined): string[] {
  return (profileValue ?? "")
    .split(",")
    .map((profile) => profile.trim())
    .filter((profile) => profile.length > 0);
}

export function hasDisabledProfile(
  profileValue: string | undefined,
  disabledProfiles: string[] | undefined,
): boolean {
  const disabled = new Set(disabledProfiles ?? []);
  return parseProfiles(profileValue).some((profile) => disabled.has(profile));
}

export function profileSchedulePath(basePath: string, profile: string): string {
  const slashIndex = Math.max(basePath.lastIndexOf("/"), basePath.lastIndexOf("\\"));
  const dotIndex = basePath.lastIndexOf(".");
  const extensionIndex = dotIndex > slashIndex ? dotIndex : basePath.length;
  return `${basePath.slice(0, extensionIndex)}-${profile}${basePath.slice(extensionIndex)}`;
}

export function resolveSchedulePath(
  basePath: string,
  profileValue: string | undefined,
  pathExists: PathExists,
): string {
  for (const profile of parseProfiles(profileValue)) {
    const candidate = profileSchedulePath(basePath, profile);
    if (pathExists(candidate)) {
      return candidate;
    }
  }
  return basePath;
}
