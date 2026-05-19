import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Find the base64 string so we can reuse it
match_b64 = re.search(r'<img src="(data:image/jpeg;base64,.*?)" alt="Diallo Ousmane"', content)
if match_b64:
    base64_str = match_b64.group(1)
else:
    # try to find it in another way
    match_b64 = re.search(r'<img src="(data:image/jpeg;base64,.*?)"', content)
    base64_str = match_b64.group(1) if match_b64 else ""

# 2. Add the state and useEffect
state_code = """
  const [currentImageIndex, setCurrentImageIndex] = useState(0);
  
  const profileImages = [
    "` + base64_str + `",
    "Photos images/2kstudio-502@1763228990.jpg",
    "Photos images/Miniature 5 postulats.jpeg",
    "Photos images/WhatsApp Image 2025-11-30 à 22.59.48_cefd7c82.jpg",
    "Photos images/WhatsApp Image 2025-11-30 à 23.00.59_a8f77c37.jpg",
    "Photos images/WhatsApp Image 2025-11-30 à 23.02.16_c25e79c7.jpg",
    "Photos images/[000614].jpg",
    "Photos images/[001069].jpg",
    "Photos images/[001118].png",
    "Photos images/[001187].jpg",
    "Photos images/[001305].jpg",
    "Photos images/[001327].jpg",
    "Photos images/[001638].jpg",
    "Photos images/im ous.jpeg"
  ];

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentImageIndex((prev) => (prev + 1) % profileImages.length);
    }, 3000);
    return () => clearInterval(interval);
  }, []);
"""

# Only add if not already there
if "const [currentImageIndex" not in content:
    content = content.replace(
        "const [isGenerating, setIsGenerating] = useState(false);",
        "const [isGenerating, setIsGenerating] = useState(false);" + state_code
    )

# 3. Replace the img tag in the hero section with the slider
# We need to find the specific img tag inside the hero-element div
hero_img_pattern = r'<div className="hero-element w-32 h-32 md:w-40 md:h-40 rounded-3xl bg-textDark border-2 border-accent mb-8 flex items-center justify-center overflow-hidden relative shadow-\[0_0_30px_rgba\(123,97,255,0\.3\)\]">\s*<img src="data:image/jpeg;base64,.*?" alt="Diallo Ousmane" className="w-full h-full object-cover" style={{ objectPosition: \'center 15%\' }} />\s*</div>'

slider_code = """<div className="hero-element w-32 h-32 md:w-40 md:h-40 rounded-3xl bg-textDark border-2 border-accent mb-8 flex items-center justify-center overflow-hidden relative shadow-[0_0_30px_rgba(123,97,255,0.3)]">
            {profileImages.map((imgSrc, index) => (
              <img
                key={index}
                src={imgSrc}
                alt={`Diallo Ousmane ${index}`}
                className="w-full h-full object-cover absolute top-0 left-0 transition-opacity duration-1000 ease-in-out"
                style={{
                  objectPosition: 'center 15%',
                  opacity: currentImageIndex === index ? 1 : 0,
                  zIndex: currentImageIndex === index ? 10 : 0
                }}
              />
            ))}
          </div>"""

# Ensure we replace exactly the hero element
content = re.sub(hero_img_pattern, slider_code, content, flags=re.DOTALL)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated App.jsx successfully.")
