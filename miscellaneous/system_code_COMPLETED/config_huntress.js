const fonts = {
  coptic: {
    // The script the Gnostic codices were written in
    glyphMSDFURL: "assets/coptic_msdf.png",
    glyphSequenceLength: 32,
    glyphTextureGridSize: [8, 8],
  },
  gothic: {
    // The script the Codex Argenteus was written in
    glyphMSDFURL: "assets/gothic_msdf.png",
    glyphSequenceLength: 27,
    glyphTextureGridSize: [8, 8],
  },
  matrixcode: {
    // The glyphs seen in the film trilogy
    glyphMSDFURL: "assets/matrixcode_msdf.png",
    glyphSequenceLength: 57,
    glyphTextureGridSize: [8, 8],
  },
  megacity: {
    // The glyphs seen in the film trilogy
    glyphMSDFURL: "assets/megacity_msdf.png",
    glyphSequenceLength: 64,
    glyphTextureGridSize: [8, 8],
  },
  resurrections: {
    // The glyphs seen in the film trilogy
    glyphMSDFURL: "assets/resurrections_msdf.png",
    glintMSDFURL: "assets/resurrections_glint_msdf.png",
    glyphSequenceLength: 135,
    glyphTextureGridSize: [13, 12],
  },
  huberfishA: {
    glyphMSDFURL: "assets/huberfish_a_msdf.png",
    glyphSequenceLength: 34,
    glyphTextureGridSize: [6, 6],
  },
  huberfishD: {
    glyphMSDFURL: "assets/huberfish_d_msdf.png",
    glyphSequenceLength: 34,
    glyphTextureGridSize: [6, 6],
  },
  gtarg_tenretniolleh: {
    glyphMSDFURL: "assets/gtarg_tenretniolleh_msdf.png",
    glyphSequenceLength: 36,
    glyphTextureGridSize: [6, 6],
  },
  gtarg_alientext: {
    glyphMSDFURL: "assets/gtarg_alientext_msdf.png",
    glyphSequenceLength: 38,
    glyphTextureGridSize: [8, 5],
  },
  neomatrixology: {
    glyphMSDFURL: "assets/neomatrixology_msdf.png",
    glyphSequenceLength: 12,
    glyphTextureGridSize: [4, 4],
  },
};

const textureURLs = {
  sand: "assets/sand.png",
  pixels: "assets/pixel_grid.png",
  mesh: "assets/mesh.png",
  metal: "assets/metal.png",
};

const hsl = (...values) => ({ space: "hsl", values });
const rgb = (...values) => ({ space: "rgb", values });

const defaults = {
  font: "matrixcode",
  effect: "palette", // The name of the effect to apply at the end of the process— mainly handles coloration
  baseTexture: null, // The name of the texture to apply to the base layer of the glyphs
  glintTexture: null, // The name of the texture to apply to the glint layer of the glyphs
  useCamera: false,
  backgroundColor: hsl(0, 0, 0), // The color "behind" the glyphs
  isolateCursor: true, // Whether the "cursor"— the brightest glyph at the bottom of a raindrop— has its own color
  cursorColor: hsl(0.242, 1, 0.73), // The color of the cursor
  cursorIntensity: 2, // The intensity of the cursor
  isolateGlint: false, // Whether the "glint"— highlights on certain symbols in the font— should appear
  glintColor: hsl(0, 0, 1), // The color of the glint
  glintIntensity: 1, // The intensity of the glint
  volumetric: false, // A mode where the raindrops appear in perspective
  animationSpeed: 1, // The global rate that all animations progress
  fps: 60, // The target frame rate (frames per second) of the effect
  forwardSpeed: 0.25, // The speed volumetric rain approaches the eye
  bloomStrength: 0.7, // The intensity of the bloom
  bloomSize: 0.4, // The amount the bloom calculation is scaled
  highPassThreshold: 0.1, // The minimum brightness that is still blurred
  cycleSpeed: 0.03, // The speed glyphs change
  cycleFrameSkip: 1, // The global minimum number of frames between glyphs cycling
  baseBrightness: -0.5, // The brightness of the glyphs, before any effects are applied
  baseContrast: 1.1, // The contrast of the glyphs, before any effects are applied
  glintBrightness: -1.5, // The brightness of the glints, before any effects are applied
  glintContrast: 2.5, // The contrast of the glints, before any effects are applied
  brightnessOverride: 0.0, // A global override to the brightness of displayed glyphs. Only used if it is > 0.
  brightnessThreshold: 0, // The minimum brightness for a glyph to still be considered visible
  brightnessDecay: 1.0, // The rate at which glyphs light up and dim
  ditherMagnitude: 0.05, // The magnitude of the random per-pixel dimming
  fallSpeed: 0.3, // The speed the raindrops progress downwards
  glyphEdgeCrop: 0.0, // The border around a glyph in a font texture that should be cropped out
  glyphHeightToWidth: 1, // The aspect ratio of glyphs
  glyphVerticalSpacing: 1, // The ratio of the vertical distance between glyphs to their height
  glyphFlip: false, // Whether to horizontally reflect the glyphs
  glyphRotation: 0, // An angle to rotate the glyphs. Currently limited to 90° increments
  hasThunder: false, // An effect that adds dramatic lightning flashes
  isPolar: false, // Whether the glyphs arc across the screen or sit in a standard grid
  rippleTypeName: null, // The variety of the ripple effect
  rippleThickness: 0.2, // The thickness of the ripple effect
  rippleScale: 30, // The size of the ripple effect
  rippleSpeed: 0.2, // The rate at which the ripple effect progresses
  numColumns: 80, // The maximum dimension of the glyph grid
  density: 1, // In volumetric mode, the number of actual columns compared to the grid
  palette: [
    // The color palette that glyph brightness is color mapped to
    { color: hsl(0.3, 0.9, 0.0), at: 0.0 },
    { color: hsl(0.3, 0.9, 0.2), at: 0.2 },
    { color: hsl(0.3, 0.9, 0.7), at: 0.7 },
    { color: hsl(0.3, 0.9, 0.8), at: 0.8 },
  ],
  raindropLength: 0.75, // Adjusts the frequency of raindrops (and their length) in a column
  slant: 0, // The angle at which rain falls; the orientation of the glyph grid
  resolution: 0.75, // An overall scale multiplier
  useHalfFloat: false,
  renderer: "regl", // The preferred web graphics API
  suppressWarnings: false, // Whether to show warnings to visitors on load
  backupGlyphsTwr: ["a", "b", "c", "d", "e", "f"], // The characters to fallback to if glyphs fail to load
  isometric: false,
  useHoloplay: false,
  loops: false,
  skipIntro: true,
  testFix: null,
};

const versions = {
  classic: {
    font: "resurrections",
    glintTexture: "mesh",
    baseTexture: "metal",
    glyphEdgeCrop: 0.1,
    cursorColor: hsl(0.333, 1, 0.85),
    cursorIntensity: 2,
    isolateGlint: true,
    glintColor: hsl(0.4, 1, 0.5),
    glintIntensity: 2,
    glintBrightness: -1.5,
    glintContrast: 3,
    baseBrightness: -0.3,
    baseContrast: 1.5,
    highPassThreshold: 0,
    numColumns: 60,
    cycleSpeed: 0.03,
    bloomStrength: 0.7,
    fallSpeed: 0.3,
    palette: [
      { color: hsl(0.51, 0.74, 0.0), at: 0.0 },
      { color: hsl(0.51, 0.74, 0.5), at: 1.0 },
    ],
    cycleSpeed: 0.015,
    volumetric: true,
    forwardSpeed: 0.1,
    raindropLength: 0.4,
    density: 0.75,
  },
};
versions.throwback = versions.operator;
versions.updated = versions.resurrections;
versions["1999"] = versions.operator;
versions["2003"] = versions.classic;
versions["2021"] = versions.resurrections;

const range = (f, min = -Infinity, max = Infinity) =>
  Math.max(min, Math.min(max, f));
const nullNaN = (f) => (isNaN(f) ? null : f);

export default () => {
  const version = versions.classic;
  const fontName = [version.font, defaults.font].find((name) => name in fonts);
  const font = fonts[fontName];

  const baseTextureURL =
    textureURLs[
      [version.baseTexture, defaults.baseTexture].find(
        (name) => name in textureURLs
      )
    ];
  const hasBaseTexture = baseTextureURL != null;
  const glintTextureURL =
    textureURLs[
      [version.glintTexture, defaults.glintTexture].find(
        (name) => name in textureURLs
      )
    ];
  const hasGlintTexture = glintTextureURL != null;

  const config = {
    ...defaults,
    ...version,
    ...font,
    baseTextureURL,
    glintTextureURL,
    hasBaseTexture,
    hasGlintTexture,
  };

  if (config.bloomSize <= 0) {
    config.bloomStrength = 0;
  }

  return config;
};
