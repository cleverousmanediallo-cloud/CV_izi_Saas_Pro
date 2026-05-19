import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the base64 string so we can preserve it
match = re.search(r'<img src="(data:image/[^"]+)"', content)
base64_img = match.group(1) if match else ''

new_printable_cv = """      {/* Printable CV Template (Hidden behind the main content) */}
      <div style={{ position: 'absolute', top: 0, left: 0, zIndex: -100, width: '210mm' }}>
          <div id="cv-printable-template" style={{ width: '210mm', minHeight: '297mm', backgroundColor: '#ffffff', display: 'flex', flexDirection: 'row', fontFamily: '"Inter", "Helvetica Neue", Helvetica, Arial, sans-serif' }}>
              {/* Left Column */}
              <div style={{ width: '35%', backgroundColor: '#2B3A4A', color: '#ffffff', padding: '0' }}>
                  <div id="pdf-photo" style={{ width: '100%', height: '220px', overflow: 'hidden', display: 'block' }}>
                      <img src="BASE64_PLACEHOLDER" style={{ width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'center 15%' }} alt="Profil" />
                  </div>
                  
                  <div style={{ padding: '30px 25px' }}>
                      {/* CONTACT */}
                      <h3 style={{ fontSize: '14px', fontWeight: '700', letterSpacing: '2px', textTransform: 'uppercase', marginBottom: '15px', borderBottom: '1px solid rgba(255,255,255,0.3)', paddingBottom: '8px' }}>Contact</h3>
                      <div style={{ fontSize: '11px', marginBottom: '30px', lineHeight: '1.6' }}>
                          <div style={{ display: 'flex', alignItems: 'center', marginBottom: '8px' }}>
                              <span style={{ marginRight: '10px', fontSize: '12px' }}>📞</span> +224 629 70 20 61
                          </div>
                          <div style={{ display: 'flex', alignItems: 'center', marginBottom: '8px', wordBreak: 'break-all' }}>
                              <span style={{ marginRight: '10px', fontSize: '12px' }}>✉️</span> cleverousmanediallo@gmail.com
                          </div>
                          <div style={{ display: 'flex', alignItems: 'center', marginBottom: '8px' }}>
                              <span style={{ marginRight: '10px', fontSize: '12px' }}>📍</span> Conakry, commune de ratoma
                          </div>
                      </div>

                      {/* EDUCATION */}
                      <h3 style={{ fontSize: '14px', fontWeight: '700', letterSpacing: '2px', textTransform: 'uppercase', marginBottom: '15px', borderBottom: '1px solid rgba(255,255,255,0.3)', paddingBottom: '8px' }}>Formation</h3>
                      <div style={{ fontSize: '11px', marginBottom: '30px', lineHeight: '1.4' }}>
                          <div style={{ marginBottom: '12px' }}>
                              <div style={{ fontWeight: '700', fontSize: '12px', marginBottom: '2px', textTransform: 'uppercase' }}>Master 2 en Ingénierie Financière</div>
                              <div style={{ color: 'rgba(255,255,255,0.7)', marginBottom: '2px' }}>Université Nongo Conakry</div>
                              <div style={{ fontSize: '10px', color: '#a0aec0' }}>2025 - 2026</div>
                          </div>
                          <div style={{ marginBottom: '12px' }}>
                              <div style={{ fontWeight: '700', fontSize: '12px', marginBottom: '2px', textTransform: 'uppercase' }}>Master 1 en Ingénierie Financière</div>
                              <div style={{ color: 'rgba(255,255,255,0.7)', marginBottom: '2px' }}>Université Nongo Conakry</div>
                              <div style={{ fontSize: '10px', color: '#a0aec0' }}>2025 - 2026</div>
                          </div>
                          <div style={{ marginBottom: '12px' }}>
                              <div style={{ fontWeight: '700', fontSize: '12px', marginBottom: '2px', textTransform: 'uppercase' }}>Licence en Admin. des Affaires</div>
                              <div style={{ color: 'rgba(255,255,255,0.7)', marginBottom: '2px' }}>Université de Kindia</div>
                              <div style={{ fontSize: '10px', color: '#a0aec0' }}>2021 - 2023</div>
                          </div>
                      </div>

                      {/* EXPERTISE */}
                      <h3 style={{ fontSize: '14px', fontWeight: '700', letterSpacing: '2px', textTransform: 'uppercase', marginBottom: '15px', borderBottom: '1px solid rgba(255,255,255,0.3)', paddingBottom: '8px' }}>Expertise</h3>
                      <ul style={{ fontSize: '11px', marginBottom: '30px', lineHeight: '1.6', paddingLeft: '15px', margin: '0' }}>
                          <li style={{ marginBottom: '6px' }}>Comptabilité OHADA</li>
                          <li style={{ marginBottom: '6px' }}>Sage i7 (Comptabilité, Paie & RH)</li>
                          <li style={{ marginBottom: '6px' }}>MS Excel Avancé</li>
                          <li style={{ marginBottom: '6px' }}>Traitement de la paie</li>
                          <li style={{ marginBottom: '6px' }}>Analyse financière</li>
                          <li style={{ marginBottom: '6px' }}>ERP Odoo</li>
                      </ul>

                      {/* LANGUES */}
                      <h3 style={{ fontSize: '14px', fontWeight: '700', letterSpacing: '2px', textTransform: 'uppercase', marginBottom: '15px', borderBottom: '1px solid rgba(255,255,255,0.3)', paddingBottom: '8px' }}>Langues</h3>
                      <div style={{ fontSize: '11px', marginBottom: '15px', lineHeight: '1.6' }}>
                          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '4px' }}><span>Français</span><span>C1</span></div>
                          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '4px' }}><span>Anglais</span><span>A2</span></div>
                          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '4px' }}><span>Soussou</span><span>Maternelle</span></div>
                          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '4px' }}><span>Malinké</span><span>A2</span></div>
                      </div>
                  </div>
              </div>

              {/* Right Column */}
              <div style={{ width: '65%', padding: '40px 30px', color: '#333333', backgroundColor: '#F8F9FA' }}>
                  {/* Header */}
                  <div style={{ marginBottom: '30px' }}>
                      <h1 style={{ fontSize: '42px', fontWeight: '900', color: '#1A202C', marginBottom: '5px', letterSpacing: '2px', textTransform: 'uppercase' }}>Diallo <span style={{ color: '#2B3A4A' }}>Ousmane</span></h1>
                      <h2 style={{ fontSize: '13px', fontWeight: '600', color: '#4A5568', letterSpacing: '3px', textTransform: 'uppercase' }}>Comptable, Spécialisé en Logiciel de Gestion</h2>
                  </div>
                  
                  {/* About Me */}
                  <div style={{ marginBottom: '25px' }}>
                      <h3 style={{ fontSize: '16px', fontWeight: '800', color: '#1A202C', letterSpacing: '1px', textTransform: 'uppercase', marginBottom: '10px', display: 'flex', alignItems: 'center' }}>
                          <span style={{ width: '30px', height: '2px', backgroundColor: '#2B3A4A', marginRight: '10px', display: 'inline-block' }}></span>
                          À Propos de Moi
                      </h3>
                      <p style={{ fontSize: '11px', lineHeight: '1.6', color: '#4A5568', textAlign: 'justify' }}>
                          Comptable spécialisé en ingénierie financière, audit et contrôle de gestion, actuellement en fin de Master 2, avec plus de deux ans d’expérience en comptabilité générale et gestion financière. Maîtrise des normes OHADA, des logiciels Sage (Comptabilité & Paie) ainsi que d’Excel avancé. Rigoureux, organisé et orienté résultats.
                      </p>
                  </div>

                  {/* Work Experience */}
                  <div style={{ marginBottom: '25px' }}>
                      <h3 style={{ fontSize: '16px', fontWeight: '800', color: '#1A202C', letterSpacing: '1px', textTransform: 'uppercase', marginBottom: '15px', display: 'flex', alignItems: 'center' }}>
                          <span style={{ width: '30px', height: '2px', backgroundColor: '#2B3A4A', marginRight: '10px', display: 'inline-block' }}></span>
                          Expérience Professionnelle
                      </h3>
                      
                      {/* Exp 1 */}
                      <div style={{ marginBottom: '15px' }}>
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', marginBottom: '2px' }}>
                              <h4 style={{ fontSize: '13px', fontWeight: '800', color: '#2B3A4A', textTransform: 'uppercase' }}>Comptable Général</h4>
                              <span style={{ fontSize: '10px', fontWeight: '600', color: '#718096' }}>Fév 2025 - Présent</span>
                          </div>
                          <div style={{ fontSize: '11px', fontWeight: '700', color: '#4A5568', marginBottom: '5px' }}>KADA TECHNOLOGIE</div>
                          <ul style={{ fontSize: '11px', color: '#4A5568', paddingLeft: '15px', margin: 0, lineHeight: '1.4' }}>
                              <li style={{ marginBottom: '2px' }}>Enregistrement des opérations comptables.</li>
                              <li style={{ marginBottom: '2px' }}>Suivi de la trésorerie et rapprochements bancaires.</li>
                              <li style={{ marginBottom: '2px' }}>Clôtures mensuelles et élaboration du bilan.</li>
                          </ul>
                      </div>

                      {/* Exp 2 */}
                      <div style={{ marginBottom: '15px' }}>
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', marginBottom: '2px' }}>
                              <h4 style={{ fontSize: '13px', fontWeight: '800', color: '#2B3A4A', textTransform: 'uppercase' }}>Créateur de contenu</h4>
                              <span style={{ fontSize: '10px', fontWeight: '600', color: '#718096' }}>2025 - Présent</span>
                          </div>
                          <div style={{ fontSize: '11px', fontWeight: '700', color: '#4A5568', marginBottom: '5px' }}>SYSCOHADA</div>
                          <ul style={{ fontSize: '11px', color: '#4A5568', paddingLeft: '15px', margin: 0, lineHeight: '1.4' }}>
                              <li style={{ marginBottom: '2px' }}>Conception de contenus en comptabilité, audit et finance.</li>
                              <li style={{ marginBottom: '2px' }}>Vulgarisation de concepts financiers complexes.</li>
                          </ul>
                      </div>

                      {/* Exp 3 */}
                      <div style={{ marginBottom: '15px' }}>
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', marginBottom: '2px' }}>
                              <h4 style={{ fontSize: '13px', fontWeight: '800', color: '#2B3A4A', textTransform: 'uppercase' }}>Stagiaire</h4>
                              <span style={{ fontSize: '10px', fontWeight: '600', color: '#718096' }}>Mars 2025 - Avr 2025</span>
                          </div>
                          <div style={{ fontSize: '11px', fontWeight: '700', color: '#4A5568', marginBottom: '5px' }}>Cabinet Expertise Plus</div>
                          <ul style={{ fontSize: '11px', color: '#4A5568', paddingLeft: '15px', margin: 0, lineHeight: '1.4' }}>
                              <li style={{ marginBottom: '2px' }}>Saisie comptable, rapprochements bancaires et suivi de caisse.</li>
                          </ul>
                      </div>
                  </div>

                  {/* Certifications */}
                  <div>
                      <h3 style={{ fontSize: '16px', fontWeight: '800', color: '#1A202C', letterSpacing: '1px', textTransform: 'uppercase', marginBottom: '15px', display: 'flex', alignItems: 'center' }}>
                          <span style={{ width: '30px', height: '2px', backgroundColor: '#2B3A4A', marginRight: '10px', display: 'inline-block' }}></span>
                          Certifications
                      </h3>
                      
                      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
                          <div style={{ marginBottom: '8px' }}>
                              <div style={{ fontSize: '12px', fontWeight: '800', color: '#2B3A4A' }}>SAP FI/CO</div>
                              <div style={{ fontSize: '10px', color: '#718096' }}>Cabinet PK Consulting (2026)</div>
                          </div>
                          <div style={{ marginBottom: '8px' }}>
                              <div style={{ fontSize: '12px', fontWeight: '800', color: '#2B3A4A' }}>ERP Odoo</div>
                              <div style={{ fontSize: '10px', color: '#718096' }}>Truculence Academy (2026)</div>
                          </div>
                          <div style={{ marginBottom: '8px' }}>
                              <div style={{ fontSize: '12px', fontWeight: '800', color: '#2B3A4A' }}>Comptabilité & Sage</div>
                              <div style={{ fontSize: '10px', color: '#718096' }}>Cabinet Expertise Plus (2025)</div>
                          </div>
                          <div style={{ marginBottom: '8px' }}>
                              <div style={{ fontSize: '12px', fontWeight: '800', color: '#2B3A4A' }}>Certificat Pro - AFC</div>
                              <div style={{ fontSize: '10px', color: '#718096' }}>Ouagadougou</div>
                          </div>
                      </div>
                  </div>

              </div>
          </div>
      </div>
"""

new_printable_cv = new_printable_cv.replace('BASE64_PLACEHOLDER', base64_img)

# Use regex to replace everything between {/* Printable CV Template */} and <div ref={mainRef}
pattern = re.compile(r'\{\/\* Printable CV Template.*?\n      <div ref=\{mainRef\}', re.DOTALL)
new_content = pattern.sub(new_printable_cv + '      <div ref={mainRef}', content)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated App.jsx successfully.")
