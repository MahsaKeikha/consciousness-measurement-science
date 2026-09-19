from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "docs" / "figures"

ARCHITECTURE = r'''<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="1180" viewBox="0 0 1800 1180">
<defs><filter id="shadow" x="-10%" y="-10%" width="120%" height="130%"><feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="#1f2e42" flood-opacity="0.07"/></filter><linearGradient id="header" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#13243a"/><stop offset="100%" stop-color="#244c64"/></linearGradient></defs>
<rect x="0" y="0" width="1800" height="1180" rx="0" fill="#f6f8fb" stroke="none" stroke-width="0" />
<rect x="0" y="0" width="1800" height="158" fill="url(#header)"/>
<text x="76" y="58" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="14" font-weight="700" fill="#b8d2e8">RESEARCH III  ·  V16-V55</text>
<text x="76" y="102" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="36" font-weight="750" fill="#ffffff">Measurement architecture and scientific decision path</text>
<text x="76" y="136" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="17" font-weight="400" fill="#d9e4ef">Eight linked validation layers connect physical observables to inference, replication, transport, and explicit stop rules.</text>
<rect x="1452" y="54" width="270" height="34" rx="17" fill="#e8f0f7" stroke="none" stroke-width="0" /><text x="1587" y="77" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#244c64">SYNTHESIS FIGURE</text>
<text x="76" y="204" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="18" font-weight="650" fill="#13243a">The program is organized as a chain of questions, not a ladder of claims.</text>
<text x="76" y="233" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="15" font-weight="400" fill="#647184">Each stage must pass its own mathematical and statistical gate before information can move downstream.</text>
<g filter="url(#shadow)">
<rect x="76" y="275" width="365" height="286" rx="20" fill="#ffffff" stroke="#d6dde7" stroke-width="1.2" />
</g>
<rect x="76" y="275" width="8" height="286" rx="4" fill="#315c7d" stroke="none" stroke-width="0" />
<rect x="100" y="297" width="90" height="34" rx="17" fill="#edf2f7" stroke="none" stroke-width="0" /><text x="145" y="320" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315c7d">V16-V20</text>
<text x="100" y="357" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="22" font-weight="750" fill="#13243a">Field observables</text>
<text x="100" y="391" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#315c7d">SCIENTIFIC QUESTION</text>
<text x="100" y="415" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="400" fill="#647184">Physical identity, invariance, confounds</text>
<text x="100" y="465" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#315c7d">CORE MATHEMATICAL OBJECT</text>
<text x="100" y="489" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="600" fill="#13243a">u, S, normalized organization features</text>
<line x1="100" y1="519" x2="417" y2="519" stroke="#e4e9ef" stroke-width="1"/>
<text x="100" y="541" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#9a3f4f">FAILURE GATE</text>
<text x="100" y="563" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="400" fill="#5c6674">Reject interpretation if nuisance structure can mimic t</text><text x="100" y="580" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="400" fill="#5c6674">he effect</text>
<g filter="url(#shadow)">
<rect x="501" y="275" width="365" height="286" rx="20" fill="#ffffff" stroke="#d6dde7" stroke-width="1.2" />
</g>
<rect x="501" y="275" width="8" height="286" rx="4" fill="#2f6b68" stroke="none" stroke-width="0" />
<rect x="525" y="297" width="90" height="34" rx="17" fill="#edf2f7" stroke="none" stroke-width="0" /><text x="570" y="320" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#2f6b68">V21-V25</text>
<text x="525" y="357" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="22" font-weight="750" fill="#13243a">Source identifiability</text>
<text x="525" y="391" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#2f6b68">SCIENTIFIC QUESTION</text>
<text x="525" y="415" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="400" fill="#647184">Forward model, null spaces, inverse sensitivity</text>
<text x="525" y="465" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#2f6b68">CORE MATHEMATICAL OBJECT</text>
<text x="525" y="489" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="600" fill="#13243a">rank(G), null(G), regularization path</text>
<line x1="525" y1="519" x2="842" y2="519" stroke="#e4e9ef" stroke-width="1"/>
<text x="525" y="541" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#9a3f4f">FAILURE GATE</text>
<text x="525" y="563" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="400" fill="#5c6674">Do not infer unique sources when the lead field is non-</text><text x="525" y="580" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="400" fill="#5c6674">identifiable</text>
<g filter="url(#shadow)">
<rect x="926" y="275" width="365" height="286" rx="20" fill="#ffffff" stroke="#d6dde7" stroke-width="1.2" />
</g>
<rect x="926" y="275" width="8" height="286" rx="4" fill="#4c6b43" stroke="none" stroke-width="0" />
<rect x="950" y="297" width="90" height="34" rx="17" fill="#edf2f7" stroke="none" stroke-width="0" /><text x="995" y="320" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#4c6b43">V26-V30</text>
<text x="950" y="357" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="22" font-weight="750" fill="#13243a">Resolution &amp; information</text>
<text x="950" y="391" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#4c6b43">SCIENTIFIC QUESTION</text>
<text x="950" y="415" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="400" fill="#647184">Noise geometry, Fisher information, aliasing</text>
<text x="950" y="465" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#4c6b43">CORE MATHEMATICAL OBJECT</text>
<text x="950" y="489" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="600" fill="#13243a">rᵀΣ⁻¹r, F = GᵀΣ⁻¹G, 1/σmin</text>
<line x1="950" y1="519" x2="1267" y2="519" stroke="#e4e9ef" stroke-width="1"/>
<text x="950" y="541" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#9a3f4f">FAILURE GATE</text>
<text x="950" y="563" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="400" fill="#5c6674">Stop when resolution, sampling, or conditioning is inad</text><text x="950" y="580" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="400" fill="#5c6674">equate</text>
<g filter="url(#shadow)">
<rect x="1351" y="275" width="365" height="286" rx="20" fill="#ffffff" stroke="#d6dde7" stroke-width="1.2" />
</g>
<rect x="1351" y="275" width="8" height="286" rx="4" fill="#74465f" stroke="none" stroke-width="0" />
<rect x="1375" y="297" width="90" height="34" rx="17" fill="#edf2f7" stroke="none" stroke-width="0" /><text x="1420" y="320" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#74465f">V31-V35</text>
<text x="1375" y="357" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="22" font-weight="750" fill="#13243a">Design &amp; specificity</text>
<text x="1375" y="391" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#74465f">SCIENTIFIC QUESTION</text>
<text x="1375" y="415" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="400" fill="#647184">PSF/CTF, sensor design, nuisance geometry</text>
<text x="1375" y="465" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#74465f">CORE MATHEMATICAL OBJECT</text>
<text x="1375" y="489" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="600" fill="#13243a">D/E-optimality, principal angles, robust i</text><text x="1375" y="508" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="600" fill="#13243a">nformation</text>
<line x1="1375" y1="519" x2="1692" y2="519" stroke="#e4e9ef" stroke-width="1"/>
<text x="1375" y="541" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#9a3f4f">FAILURE GATE</text>
<text x="1375" y="563" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="400" fill="#5c6674">Prefer designs that preserve target information under n</text><text x="1375" y="580" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="400" fill="#5c6674">uisance/model uncertainty</text>
<g filter="url(#shadow)">
<rect x="76" y="618" width="365" height="286" rx="20" fill="#ffffff" stroke="#d6dde7" stroke-width="1.2" />
</g>
<rect x="76" y="618" width="8" height="286" rx="4" fill="#8a672f" stroke="none" stroke-width="0" />
<rect x="100" y="640" width="90" height="34" rx="17" fill="#edf2f7" stroke="none" stroke-width="0" /><text x="145" y="663" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#8a672f">V36-V40</text>
<text x="100" y="700" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="22" font-weight="750" fill="#13243a">Finite-sample inference</text>
<text x="100" y="734" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#8a672f">SCIENTIFIC QUESTION</text>
<text x="100" y="758" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="400" fill="#647184">GLS, CRLB, discrimination, FWER, sandwich va</text><text x="100" y="777" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="400" fill="#647184">riance</text>
<text x="100" y="808" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#8a672f">CORE MATHEMATICAL OBJECT</text>
<text x="100" y="832" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="600" fill="#13243a">Var(â), Bayes error, multiplicity thresholds</text>
<line x1="100" y1="862" x2="417" y2="862" stroke="#e4e9ef" stroke-width="1"/>
<text x="100" y="884" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#9a3f4f">FAILURE GATE</text>
<text x="100" y="906" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="400" fill="#5c6674">Report calibrated uncertainty, not point estimates alone</text>
<g filter="url(#shadow)">
<rect x="501" y="618" width="365" height="286" rx="20" fill="#ffffff" stroke="#d6dde7" stroke-width="1.2" />
</g>
<rect x="501" y="618" width="8" height="286" rx="4" fill="#315c7d" stroke="none" stroke-width="0" />
<rect x="525" y="640" width="90" height="34" rx="17" fill="#edf2f7" stroke="none" stroke-width="0" /><text x="570" y="663" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315c7d">V41-V45</text>
<text x="525" y="700" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="22" font-weight="750" fill="#13243a">Selection-safe inference</text>
<text x="525" y="734" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#315c7d">SCIENTIFIC QUESTION</text>
<text x="525" y="758" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="400" fill="#647184">Bonferroni, Holm, exact randomization, holdout</text>
<text x="525" y="808" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#315c7d">CORE MATHEMATICAL OBJECT</text>
<text x="525" y="832" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="600" fill="#13243a">FWER, max-statistic, post-selection coverage</text>
<line x1="525" y1="862" x2="842" y2="862" stroke="#e4e9ef" stroke-width="1"/>
<text x="525" y="884" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#9a3f4f">FAILURE GATE</text>
<text x="525" y="906" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="400" fill="#5c6674">Require independent confirmation after search/selection</text>
<g filter="url(#shadow)">
<rect x="926" y="618" width="365" height="286" rx="20" fill="#ffffff" stroke="#d6dde7" stroke-width="1.2" />
</g>
<rect x="926" y="618" width="8" height="286" rx="4" fill="#2f6b68" stroke="none" stroke-width="0" />
<rect x="950" y="640" width="90" height="34" rx="17" fill="#edf2f7" stroke="none" stroke-width="0" /><text x="995" y="663" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#2f6b68">V46-V50</text>
<text x="950" y="700" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="22" font-weight="750" fill="#13243a">Replication stability</text>
<text x="950" y="734" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#2f6b68">SCIENTIFIC QUESTION</text>
<text x="950" y="758" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="400" fill="#647184">Pooling, heterogeneity, leave-one-site-out, </text><text x="950" y="777" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="400" fill="#647184">partial conjunction</text>
<text x="950" y="808" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#2f6b68">CORE MATHEMATICAL OBJECT</text>
<text x="950" y="832" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="600" fill="#13243a">Q, effective sites, delete-one influence</text>
<line x1="950" y1="862" x2="1267" y2="862" stroke="#e4e9ef" stroke-width="1"/>
<text x="950" y="884" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#9a3f4f">FAILURE GATE</text>
<text x="950" y="906" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="400" fill="#5c6674">Reject fragile findings dominated by one site or incons</text><text x="950" y="923" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="400" fill="#5c6674">istent replication</text>
<g filter="url(#shadow)">
<rect x="1351" y="618" width="365" height="286" rx="20" fill="#ffffff" stroke="#d6dde7" stroke-width="1.2" />
</g>
<rect x="1351" y="618" width="8" height="286" rx="4" fill="#4c6b43" stroke="none" stroke-width="0" />
<rect x="1375" y="640" width="90" height="34" rx="17" fill="#edf2f7" stroke="none" stroke-width="0" /><text x="1420" y="663" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#4c6b43">V51-V55</text>
<text x="1375" y="700" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="22" font-weight="750" fill="#13243a">Transportability</text>
<text x="1375" y="734" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#4c6b43">SCIENTIFIC QUESTION</text>
<text x="1375" y="758" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="400" fill="#647184">Coordinate invariance, projection loss, shif</text><text x="1375" y="777" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="400" fill="#647184">t sensitivity</text>
<text x="1375" y="808" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#4c6b43">CORE MATHEMATICAL OBJECT</text>
<text x="1375" y="832" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="600" fill="#13243a">information fraction, importance weights, </text><text x="1375" y="851" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="600" fill="#13243a">TV bound</text>
<line x1="1375" y1="862" x2="1692" y2="862" stroke="#e4e9ef" stroke-width="1"/>
<text x="1375" y="884" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="11" font-weight="750" fill="#9a3f4f">FAILURE GATE</text>
<text x="1375" y="906" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="400" fill="#5c6674">Abstain when transport assumptions or overlap are insuf</text><text x="1375" y="923" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="400" fill="#5c6674">ficient</text>
<line x1="449" y1="418" x2="491" y2="418" stroke="#9aa7b6" stroke-width="2"/><path d="M 481 412 L 491 418 L 481 424" fill="none" stroke="#9aa7b6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<line x1="874" y1="418" x2="916" y2="418" stroke="#9aa7b6" stroke-width="2"/><path d="M 906 412 L 916 418 L 906 424" fill="none" stroke="#9aa7b6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<line x1="1299" y1="418" x2="1341" y2="418" stroke="#9aa7b6" stroke-width="2"/><path d="M 1331 412 L 1341 418 L 1331 424" fill="none" stroke="#9aa7b6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<line x1="449" y1="761" x2="491" y2="761" stroke="#9aa7b6" stroke-width="2"/><path d="M 481 755 L 491 761 L 481 767" fill="none" stroke="#9aa7b6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<line x1="874" y1="761" x2="916" y2="761" stroke="#9aa7b6" stroke-width="2"/><path d="M 906 755 L 916 761 L 906 767" fill="none" stroke="#9aa7b6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<line x1="1299" y1="761" x2="1341" y2="761" stroke="#9aa7b6" stroke-width="2"/><path d="M 1331 755 L 1341 761 L 1331 767" fill="none" stroke="#9aa7b6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<line x1="1716" y1="573" x2="1716" y2="604" stroke="#9aa7b6" stroke-width="2"/><path d="M 1706 598 L 1716 604 L 1706 610" fill="none" stroke="#9aa7b6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<text x="76" y="955" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="750" fill="#74465f">CLAIM-CONTROL SPINE</text>
<rect x="76" y="976" width="1648" height="116" rx="18" fill="#ffffff" stroke="#d4dce6" stroke-width="1.2" />
<rect x="105" y="998" width="42" height="34" rx="17" fill="#e7eff5" stroke="none" stroke-width="0" /><text x="126" y="1021" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315c7d">1</text>
<text x="163" y="1019" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="15" font-weight="750" fill="#13243a">Measure</text>
<text x="163" y="1044" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="400" fill="#647184">Is the observable physically and instr</text><text x="163" y="1061" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="400" fill="#647184">umentally well defined?</text>
<line x1="487" y1="1005" x2="487" y2="1070" stroke="#e3e8ef" stroke-width="1"/>
<rect x="509" y="998" width="42" height="34" rx="17" fill="#e7eff5" stroke="none" stroke-width="0" /><text x="530" y="1021" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315c7d">2</text>
<text x="567" y="1019" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="15" font-weight="750" fill="#13243a">Identify</text>
<text x="567" y="1044" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="400" fill="#647184">Is the latent/source target identifiab</text><text x="567" y="1061" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="400" fill="#647184">le under the declared model?</text>
<line x1="891" y1="1005" x2="891" y2="1070" stroke="#e3e8ef" stroke-width="1"/>
<rect x="913" y="998" width="42" height="34" rx="17" fill="#f3ecef" stroke="none" stroke-width="0" /><text x="934" y="1021" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#74465f">3</text>
<text x="971" y="1019" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="15" font-weight="750" fill="#13243a">Infer</text>
<text x="971" y="1044" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="400" fill="#647184">Are uncertainty, multiplicity, and sel</text><text x="971" y="1061" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="400" fill="#647184">ection handled correctly?</text>
<line x1="1295" y1="1005" x2="1295" y2="1070" stroke="#e3e8ef" stroke-width="1"/>
<rect x="1317" y="998" width="42" height="34" rx="17" fill="#f3ecef" stroke="none" stroke-width="0" /><text x="1338" y="1021" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#74465f">4</text>
<text x="1375" y="1019" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="15" font-weight="750" fill="#13243a">Generalize</text>
<text x="1375" y="1044" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="400" fill="#647184">Does the result replicate and transpor</text><text x="1375" y="1061" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="400" fill="#647184">t without hidden instability?</text>
<text x="76" y="1143" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="500" fill="#6a7584">Scope boundary: analytic and synthetic validation of measurement machinery. No stage by itself constitutes empirical evidence that consciousness has been measured.</text>
</svg>'''
UNCERTAINTY = r'''<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="1040" viewBox="0 0 1800 1040">
<defs><linearGradient id="h2" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#13243a"/><stop offset="100%" stop-color="#315c7d"/></linearGradient><filter id="s2"><feDropShadow dx="0" dy="5" stdDeviation="9" flood-color="#1d2b3f" flood-opacity="0.06"/></filter></defs>
<rect x="0" y="0" width="1800" height="1040" rx="0" fill="#f7f9fc" stroke="none" stroke-width="0" />
<rect x="0" y="0" width="1800" height="156" fill="url(#h2)"/>
<text x="76" y="58" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="14" font-weight="700" fill="#bdd4e8">RESEARCH III  ·  UNCERTAINTY PROPAGATION</text>
<text x="76" y="102" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="35" font-weight="750" fill="#ffffff">Where uncertainty enters, how it propagates, and where the analysis must stop</text>
<text x="76" y="136" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="17" font-weight="400" fill="#dbe5ef">The visual grammar distinguishes data uncertainty, model uncertainty, selection uncertainty, and transport uncertainty.</text>
<rect x="1465" y="54" width="260" height="34" rx="17" fill="#e8f0f7" stroke="none" stroke-width="0" /><text x="1595" y="77" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#244c64">INFERENCE MAP</text>
<g filter="url(#s2)"><rect x="76" y="238" width="370" height="100" rx="16" fill="#fff" stroke="#d6dde7" stroke-width="1.2" /></g>
<rect x="96" y="256" width="105" height="34" rx="17" fill="#edf2f7" stroke="none" stroke-width="0" /><text x="148.5" y="279" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315c7d">OBSERVATION</text>
<text x="214" y="279" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="16" font-weight="700" fill="#13243a">Sensor noise / contamination</text>
<text x="96" y="314" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="500" fill="#647184">Σ, common-mode nuisance, missingness</text>
<line x1="446" y1="288" x2="545" y2="288" stroke="#9ba7b4" stroke-width="2"/><path d="M 535 282 L 545 288 L 535 294" fill="none" stroke="#9ba7b4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<g filter="url(#s2)"><rect x="76" y="370" width="370" height="100" rx="16" fill="#fff" stroke="#d6dde7" stroke-width="1.2" /></g>
<rect x="96" y="388" width="105" height="34" rx="17" fill="#edf2f7" stroke="none" stroke-width="0" /><text x="148.5" y="411" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#2f6b68">MODEL</text>
<text x="214" y="411" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="16" font-weight="700" fill="#13243a">Reference / forward model</text>
<text x="96" y="446" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="500" fill="#647184">G, null spaces, regularization, mismatch</text>
<line x1="446" y1="420" x2="545" y2="420" stroke="#9ba7b4" stroke-width="2"/><path d="M 535 414 L 545 420 L 535 426" fill="none" stroke="#9ba7b4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<g filter="url(#s2)"><rect x="76" y="502" width="370" height="100" rx="16" fill="#fff" stroke="#d6dde7" stroke-width="1.2" /></g>
<rect x="96" y="520" width="105" height="34" rx="17" fill="#edf2f7" stroke="none" stroke-width="0" /><text x="148.5" y="543" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#74465f">SEARCH</text>
<text x="214" y="543" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="16" font-weight="700" fill="#13243a">Multiplicity / selection</text>
<text x="96" y="578" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="500" fill="#647184">m hypotheses, max statistic, holdout split</text>
<line x1="446" y1="552" x2="545" y2="552" stroke="#9ba7b4" stroke-width="2"/><path d="M 535 546 L 545 552 L 535 558" fill="none" stroke="#9ba7b4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<g filter="url(#s2)"><rect x="76" y="634" width="370" height="100" rx="16" fill="#fff" stroke="#d6dde7" stroke-width="1.2" /></g>
<rect x="96" y="652" width="105" height="34" rx="17" fill="#edf2f7" stroke="none" stroke-width="0" /><text x="148.5" y="675" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#8a672f">DOMAIN</text>
<text x="214" y="675" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="16" font-weight="700" fill="#13243a">Site / hardware / population shift</text>
<text x="96" y="710" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="500" fill="#647184">weights, overlap, total variation</text>
<line x1="446" y1="684" x2="545" y2="684" stroke="#9ba7b4" stroke-width="2"/><path d="M 535 678 L 545 684 L 535 690" fill="none" stroke="#9ba7b4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<text x="545" y="206" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="750" fill="#315c7d">PROPAGATION LAYER</text>
<g filter="url(#s2)"><rect x="545" y="238" width="390" height="100" rx="16" fill="#fff" stroke="#d6dde7" stroke-width="1.2" /></g>
<text x="569" y="276" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="18" font-weight="750" fill="#13243a">Measurement geometry</text>
<text x="569" y="310" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="600" fill="#315c7d">rᵀΣ⁻¹r  ·  whitening  ·  information retained</text>
<g filter="url(#s2)"><rect x="545" y="370" width="390" height="100" rx="16" fill="#fff" stroke="#d6dde7" stroke-width="1.2" /></g>
<text x="569" y="408" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="18" font-weight="750" fill="#13243a">Inverse / design geometry</text>
<text x="569" y="442" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="600" fill="#2f6b68">rank(G)  ·  PSF/CTF  ·  D/E-optimality</text>
<g filter="url(#s2)"><rect x="545" y="502" width="390" height="100" rx="16" fill="#fff" stroke="#d6dde7" stroke-width="1.2" /></g>
<text x="569" y="540" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="18" font-weight="750" fill="#13243a">Sampling / decision layer</text>
<text x="569" y="574" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="600" fill="#74465f">Var(â)  ·  CRLB  ·  FWER  ·  post-selection coverage</text>
<g filter="url(#s2)"><rect x="545" y="634" width="390" height="100" rx="16" fill="#fff" stroke="#d6dde7" stroke-width="1.2" /></g>
<text x="569" y="672" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="18" font-weight="750" fill="#13243a">Replication / transport layer</text>
<text x="569" y="706" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="600" fill="#8a672f">Q  ·  effective sites  ·  importance weights  ·  TV</text>
<text x="1034" y="206" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="750" fill="#74465f">DECISION GATES</text>
<g filter="url(#s2)"><rect x="1034" y="238" width="690" height="100" rx="16" fill="#fff" stroke="#d6dde7" stroke-width="1.2" /></g>
<rect x="1034" y="238" width="7" height="100" rx="3" fill="If distinct latent/source states map to the same observables, report a set or ambiguity, not a unique source." stroke="none" stroke-width="0" />
<text x="1058" y="272" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="14" font-weight="750" fill="If distinct latent/source states map to the same observables, report a set or ambiguity, not a unique source.">G1  IDENTIFIABILITY</text>
<text x="1058" y="299" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="400" fill="#647184">If distinct latent/source states map to the same observables, report a set or ambigu</text><text x="1058" y="317" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="400" fill="#647184">ity, not a unique source.</text>
<g filter="url(#s2)"><rect x="1034" y="370" width="690" height="100" rx="16" fill="#fff" stroke="#d6dde7" stroke-width="1.2" /></g>
<rect x="1034" y="370" width="7" height="100" rx="3" fill="If information collapses or inverse amplification becomes unstable, abstain or redesign the measurement." stroke="none" stroke-width="0" />
<text x="1058" y="404" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="14" font-weight="750" fill="If information collapses or inverse amplification becomes unstable, abstain or redesign the measurement.">G2  RESOLUTION / CONDITIONING</text>
<text x="1058" y="431" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="400" fill="#647184">If information collapses or inverse amplification becomes unstable, abstain or redes</text><text x="1058" y="449" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="400" fill="#647184">ign the measurement.</text>
<g filter="url(#s2)"><rect x="1034" y="502" width="690" height="100" rx="16" fill="#fff" stroke="#d6dde7" stroke-width="1.2" /></g>
<rect x="1034" y="502" width="7" height="100" rx="3" fill="Control multiplicity and separate discovery from confirmation before interpreting a selected effect." stroke="none" stroke-width="0" />
<text x="1058" y="536" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="14" font-weight="750" fill="Control multiplicity and separate discovery from confirmation before interpreting a selected effect.">G3  VALID INFERENCE AFTER SEARCH</text>
<text x="1058" y="563" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="400" fill="#647184">Control multiplicity and separate discovery from confirmation before interpreting a </text><text x="1058" y="581" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="400" fill="#647184">selected effect.</text>
<g filter="url(#s2)"><rect x="1034" y="634" width="690" height="100" rx="16" fill="#fff" stroke="#d6dde7" stroke-width="1.2" /></g>
<rect x="1034" y="634" width="7" height="100" rx="3" fill="Require stability across sites and adequate overlap before generalizing beyond the analyzed domain." stroke="none" stroke-width="0" />
<text x="1058" y="668" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="14" font-weight="750" fill="Require stability across sites and adequate overlap before generalizing beyond the analyzed domain.">G4  REPLICATION / TRANSPORT</text>
<text x="1058" y="695" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="400" fill="#647184">Require stability across sites and adequate overlap before generalizing beyond the a</text><text x="1058" y="713" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="400" fill="#647184">nalyzed domain.</text>
<rect x="76" y="790" width="1648" height="156" rx="20" fill="#ffffff" stroke="#cfd8e4" stroke-width="1.4" />
<text x="102" y="826" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="750" fill="#13243a">A reviewer should be able to trace every reported number through this chain:</text>
<rect x="102" y="852" width="150" height="34" rx="17" fill="#eef2f6" stroke="none" stroke-width="0" /><text x="177" y="875" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315c7d">OBSERVABLE RECORD</text>
<line x1="260" y1="869" x2="282" y2="869" stroke="#a5afbc" stroke-width="2"/><path d="M 272 863 L 282 869 L 272 875" fill="none" stroke="#a5afbc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="294" y="852" width="150" height="34" rx="17" fill="#eef2f6" stroke="none" stroke-width="0" /><text x="369" y="875" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315c7d">DECLARED MODEL</text>
<line x1="452" y1="869" x2="474" y2="869" stroke="#a5afbc" stroke-width="2"/><path d="M 464 863 L 474 869 L 464 875" fill="none" stroke="#a5afbc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="486" y="852" width="165" height="34" rx="17" fill="#eef2f6" stroke="none" stroke-width="0" /><text x="568.5" y="875" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#2f6b68">IDENTIFIED QUANTITY</text>
<line x1="659" y1="869" x2="681" y2="869" stroke="#a5afbc" stroke-width="2"/><path d="M 671 863 L 681 869 L 671 875" fill="none" stroke="#a5afbc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="693" y="852" width="150" height="34" rx="17" fill="#eef2f6" stroke="none" stroke-width="0" /><text x="768" y="875" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#2f6b68">UNCERTAINTY SET</text>
<line x1="851" y1="869" x2="873" y2="869" stroke="#a5afbc" stroke-width="2"/><path d="M 863 863 L 873 869 L 863 875" fill="none" stroke="#a5afbc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="885" y="852" width="205" height="34" rx="17" fill="#eef2f6" stroke="none" stroke-width="0" /><text x="987.5" y="875" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#74465f">SELECTION-SAFE DECISION</text>
<line x1="1098" y1="869" x2="1120" y2="869" stroke="#a5afbc" stroke-width="2"/><path d="M 1110 863 L 1120 869 L 1110 875" fill="none" stroke="#a5afbc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="1132" y="852" width="250" height="34" rx="17" fill="#eef2f6" stroke="none" stroke-width="0" /><text x="1257" y="875" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#74465f">REPLICATION / TRANSPORT BOUNDARY</text>
<text x="102" y="922" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="14" font-weight="650" fill="#13243a">Core rule: uncertainty is not a footnote. It is propagated until it either supports the declared claim or forces abstention.</text>
<text x="76" y="1000" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="500" fill="#6a7584">Scope boundary: this map formalizes uncertainty handling in the analytic/synthetic program. Empirical validity for consciousness-related targets remains a separate scientific burden.</text>
</svg>'''
MATURITY = r'''<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="1120" viewBox="0 0 1800 1120">
<defs><linearGradient id="h3" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#13243a"/><stop offset="100%" stop-color="#2f6b68"/></linearGradient></defs>
<rect x="0" y="0" width="1800" height="1120" rx="0" fill="#f7f9fc" stroke="none" stroke-width="0" />
<rect x="0" y="0" width="1800" height="156" fill="url(#h3)"/>
<text x="76" y="58" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="14" font-weight="700" fill="#bfe0dc">RESEARCH III  ·  VALIDATION MATURITY MATRIX</text>
<text x="76" y="102" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="35" font-weight="750" fill="#ffffff">What is established now, what is stress-tested, and what remains scientifically open</text>
<text x="76" y="136" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="17" font-weight="400" fill="#dcece9">Maturity is represented by explicit evidence layers rather than by a single confidence score.</text>
<rect x="1450" y="54" width="275" height="34" rx="17" fill="#e6f0ee" stroke="none" stroke-width="0" /><text x="1587.5" y="77" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#2f6b68">REVIEWER ORIENTATION</text>
<rect x="76" y="208" width="400" height="56" rx="10" fill="#e9eef4" stroke="#d0d8e2" stroke-width="1" />
<text x="276" y="243" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="750" fill="#13243a">Program layer</text>
<rect x="476" y="208" width="250" height="56" rx="10" fill="#e9eef4" stroke="#d0d8e2" stroke-width="1" />
<text x="601" y="243" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="750" fill="#13243a">Analytic identity / theorem</text>
<rect x="726" y="208" width="250" height="56" rx="10" fill="#e9eef4" stroke="#d0d8e2" stroke-width="1" />
<text x="851" y="243" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="750" fill="#13243a">Deterministic / synthetic stress</text>
<rect x="976" y="208" width="240" height="56" rx="10" fill="#e9eef4" stroke="#d0d8e2" stroke-width="1" />
<text x="1096" y="243" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="750" fill="#13243a">Uncertainty quantified</text>
<rect x="1216" y="208" width="240" height="56" rx="10" fill="#e9eef4" stroke="#d0d8e2" stroke-width="1" />
<text x="1336" y="243" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="750" fill="#13243a">Failure / abstention gate</text>
<rect x="1456" y="208" width="268" height="56" rx="10" fill="#e9eef4" stroke="#d0d8e2" stroke-width="1" />
<text x="1590" y="243" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="13" font-weight="750" fill="#13243a">External empirical validation</text>
<rect x="76" y="284" width="1648" height="64" rx="8" fill="#ffffff" stroke="#dfe5ec" stroke-width="1" />
<rect x="92" y="299" width="82" height="34" rx="17" fill="#edf2f7" stroke="none" stroke-width="0" /><text x="133" y="322" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315c7d">V16-V20</text>
<text x="188" y="323" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="15" font-weight="700" fill="#13243a">Field observables &amp; confounds</text>
<rect x="526" y="299" width="150" height="34" rx="17" fill="#e7f0f5" stroke="none" stroke-width="0" /><text x="601" y="322" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315c7d">ESTABLISHED</text>
<rect x="776" y="299" width="150" height="34" rx="17" fill="#e7f2ef" stroke="none" stroke-width="0" /><text x="851" y="322" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#2f6b68">STRESS-TESTED</text>
<rect x="1021" y="299" width="150" height="34" rx="17" fill="#eef2e8" stroke="none" stroke-width="0" /><text x="1096" y="322" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#4c6b43">QUANTIFIED</text>
<rect x="1261" y="299" width="150" height="34" rx="17" fill="#f3ebef" stroke="none" stroke-width="0" /><text x="1336" y="322" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#74465f">EXPLICIT GATE</text>
<rect x="1515" y="299" width="150" height="34" rx="17" fill="#fff4df" stroke="none" stroke-width="0" /><text x="1590" y="322" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#8a672f">OPEN</text>
<rect x="76" y="362" width="1648" height="64" rx="8" fill="#fbfcfe" stroke="#dfe5ec" stroke-width="1" />
<rect x="92" y="377" width="82" height="34" rx="17" fill="#edf2f7" stroke="none" stroke-width="0" /><text x="133" y="400" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315c7d">V21-V25</text>
<text x="188" y="401" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="15" font-weight="700" fill="#13243a">Source identifiability</text>
<rect x="526" y="377" width="150" height="34" rx="17" fill="#e7f0f5" stroke="none" stroke-width="0" /><text x="601" y="400" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315c7d">ESTABLISHED</text>
<rect x="776" y="377" width="150" height="34" rx="17" fill="#e7f2ef" stroke="none" stroke-width="0" /><text x="851" y="400" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#2f6b68">STRESS-TESTED</text>
<rect x="1021" y="377" width="150" height="34" rx="17" fill="#eef2e8" stroke="none" stroke-width="0" /><text x="1096" y="400" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#4c6b43">QUANTIFIED</text>
<rect x="1261" y="377" width="150" height="34" rx="17" fill="#f3ebef" stroke="none" stroke-width="0" /><text x="1336" y="400" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#74465f">EXPLICIT GATE</text>
<rect x="1515" y="377" width="150" height="34" rx="17" fill="#fff4df" stroke="none" stroke-width="0" /><text x="1590" y="400" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#8a672f">OPEN</text>
<rect x="76" y="440" width="1648" height="64" rx="8" fill="#ffffff" stroke="#dfe5ec" stroke-width="1" />
<rect x="92" y="455" width="82" height="34" rx="17" fill="#edf2f7" stroke="none" stroke-width="0" /><text x="133" y="478" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315c7d">V26-V30</text>
<text x="188" y="479" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="15" font-weight="700" fill="#13243a">Resolution &amp; information</text>
<rect x="526" y="455" width="150" height="34" rx="17" fill="#e7f0f5" stroke="none" stroke-width="0" /><text x="601" y="478" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315c7d">ESTABLISHED</text>
<rect x="776" y="455" width="150" height="34" rx="17" fill="#e7f2ef" stroke="none" stroke-width="0" /><text x="851" y="478" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#2f6b68">STRESS-TESTED</text>
<rect x="1021" y="455" width="150" height="34" rx="17" fill="#eef2e8" stroke="none" stroke-width="0" /><text x="1096" y="478" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#4c6b43">QUANTIFIED</text>
<rect x="1261" y="455" width="150" height="34" rx="17" fill="#f3ebef" stroke="none" stroke-width="0" /><text x="1336" y="478" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#74465f">EXPLICIT GATE</text>
<rect x="1515" y="455" width="150" height="34" rx="17" fill="#fff4df" stroke="none" stroke-width="0" /><text x="1590" y="478" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#8a672f">OPEN</text>
<rect x="76" y="518" width="1648" height="64" rx="8" fill="#fbfcfe" stroke="#dfe5ec" stroke-width="1" />
<rect x="92" y="533" width="82" height="34" rx="17" fill="#edf2f7" stroke="none" stroke-width="0" /><text x="133" y="556" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315c7d">V31-V35</text>
<text x="188" y="557" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="15" font-weight="700" fill="#13243a">Design &amp; spatial specificity</text>
<rect x="526" y="533" width="150" height="34" rx="17" fill="#e7f0f5" stroke="none" stroke-width="0" /><text x="601" y="556" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315c7d">ESTABLISHED</text>
<rect x="776" y="533" width="150" height="34" rx="17" fill="#e7f2ef" stroke="none" stroke-width="0" /><text x="851" y="556" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#2f6b68">STRESS-TESTED</text>
<rect x="1021" y="533" width="150" height="34" rx="17" fill="#eef2e8" stroke="none" stroke-width="0" /><text x="1096" y="556" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#4c6b43">QUANTIFIED</text>
<rect x="1261" y="533" width="150" height="34" rx="17" fill="#f3ebef" stroke="none" stroke-width="0" /><text x="1336" y="556" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#74465f">EXPLICIT GATE</text>
<rect x="1515" y="533" width="150" height="34" rx="17" fill="#fff4df" stroke="none" stroke-width="0" /><text x="1590" y="556" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#8a672f">OPEN</text>
<rect x="76" y="596" width="1648" height="64" rx="8" fill="#ffffff" stroke="#dfe5ec" stroke-width="1" />
<rect x="92" y="611" width="82" height="34" rx="17" fill="#edf2f7" stroke="none" stroke-width="0" /><text x="133" y="634" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#2f6b68">V36-V40</text>
<text x="188" y="635" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="15" font-weight="700" fill="#13243a">Finite-sample inference</text>
<rect x="526" y="611" width="150" height="34" rx="17" fill="#e7f0f5" stroke="none" stroke-width="0" /><text x="601" y="634" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315c7d">ESTABLISHED</text>
<rect x="776" y="611" width="150" height="34" rx="17" fill="#e7f2ef" stroke="none" stroke-width="0" /><text x="851" y="634" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#2f6b68">STRESS-TESTED</text>
<rect x="1021" y="611" width="150" height="34" rx="17" fill="#eef2e8" stroke="none" stroke-width="0" /><text x="1096" y="634" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#4c6b43">QUANTIFIED</text>
<rect x="1261" y="611" width="150" height="34" rx="17" fill="#f3ebef" stroke="none" stroke-width="0" /><text x="1336" y="634" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#74465f">EXPLICIT GATE</text>
<rect x="1515" y="611" width="150" height="34" rx="17" fill="#fff4df" stroke="none" stroke-width="0" /><text x="1590" y="634" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#8a672f">OPEN</text>
<rect x="76" y="674" width="1648" height="64" rx="8" fill="#fbfcfe" stroke="#dfe5ec" stroke-width="1" />
<rect x="92" y="689" width="82" height="34" rx="17" fill="#edf2f7" stroke="none" stroke-width="0" /><text x="133" y="712" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#2f6b68">V41-V45</text>
<text x="188" y="713" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="15" font-weight="700" fill="#13243a">Selection-safe inference</text>
<rect x="526" y="689" width="150" height="34" rx="17" fill="#e7f0f5" stroke="none" stroke-width="0" /><text x="601" y="712" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315c7d">ESTABLISHED</text>
<rect x="776" y="689" width="150" height="34" rx="17" fill="#e7f2ef" stroke="none" stroke-width="0" /><text x="851" y="712" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#2f6b68">STRESS-TESTED</text>
<rect x="1021" y="689" width="150" height="34" rx="17" fill="#eef2e8" stroke="none" stroke-width="0" /><text x="1096" y="712" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#4c6b43">QUANTIFIED</text>
<rect x="1261" y="689" width="150" height="34" rx="17" fill="#f3ebef" stroke="none" stroke-width="0" /><text x="1336" y="712" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#74465f">EXPLICIT GATE</text>
<rect x="1515" y="689" width="150" height="34" rx="17" fill="#fff4df" stroke="none" stroke-width="0" /><text x="1590" y="712" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#8a672f">OPEN</text>
<rect x="76" y="752" width="1648" height="64" rx="8" fill="#ffffff" stroke="#dfe5ec" stroke-width="1" />
<rect x="92" y="767" width="82" height="34" rx="17" fill="#edf2f7" stroke="none" stroke-width="0" /><text x="133" y="790" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#2f6b68">V46-V50</text>
<text x="188" y="791" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="15" font-weight="700" fill="#13243a">Replication inference</text>
<rect x="526" y="767" width="150" height="34" rx="17" fill="#e7f0f5" stroke="none" stroke-width="0" /><text x="601" y="790" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315c7d">ESTABLISHED</text>
<rect x="776" y="767" width="150" height="34" rx="17" fill="#e7f2ef" stroke="none" stroke-width="0" /><text x="851" y="790" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#2f6b68">STRESS-TESTED</text>
<rect x="1021" y="767" width="150" height="34" rx="17" fill="#eef2e8" stroke="none" stroke-width="0" /><text x="1096" y="790" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#4c6b43">QUANTIFIED</text>
<rect x="1261" y="767" width="150" height="34" rx="17" fill="#f3ebef" stroke="none" stroke-width="0" /><text x="1336" y="790" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#74465f">EXPLICIT GATE</text>
<rect x="1515" y="767" width="150" height="34" rx="17" fill="#fff4df" stroke="none" stroke-width="0" /><text x="1590" y="790" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#8a672f">OPEN</text>
<rect x="76" y="830" width="1648" height="64" rx="8" fill="#fbfcfe" stroke="#dfe5ec" stroke-width="1" />
<rect x="92" y="845" width="82" height="34" rx="17" fill="#edf2f7" stroke="none" stroke-width="0" /><text x="133" y="868" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#2f6b68">V51-V55</text>
<text x="188" y="869" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="15" font-weight="700" fill="#13243a">Transportability</text>
<rect x="526" y="845" width="150" height="34" rx="17" fill="#e7f0f5" stroke="none" stroke-width="0" /><text x="601" y="868" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315c7d">ESTABLISHED</text>
<rect x="776" y="845" width="150" height="34" rx="17" fill="#e7f2ef" stroke="none" stroke-width="0" /><text x="851" y="868" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#2f6b68">STRESS-TESTED</text>
<rect x="1021" y="845" width="150" height="34" rx="17" fill="#eef2e8" stroke="none" stroke-width="0" /><text x="1096" y="868" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#4c6b43">QUANTIFIED</text>
<rect x="1261" y="845" width="150" height="34" rx="17" fill="#f3ebef" stroke="none" stroke-width="0" /><text x="1336" y="868" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#74465f">EXPLICIT GATE</text>
<rect x="1515" y="845" width="150" height="34" rx="17" fill="#fff4df" stroke="none" stroke-width="0" /><text x="1590" y="868" text-anchor="middle" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#8a672f">OPEN</text>
<text x="76" y="938" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="750" fill="#74465f">INTERPRETATION</text>
<rect x="76" y="960" width="1648" height="96" rx="18" fill="#ffffff" stroke="#d2dae4" stroke-width="1.2" />
<text x="102" y="993" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="16" font-weight="750" fill="#13243a">The research is mature in its mathematical control structure, not yet in empirical consciousness validation.</text>
<text x="102" y="1022" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="14" font-weight="500" fill="#647184">The next scientific milestone is not another synthetic theorem alone: it is preregistered, multimodal, human or system-level data that can challenge these gates under real measurement conditions.</text>
<text x="76" y="1090" text-anchor="start" font-family="Inter, Arial, Helvetica, sans-serif" font-size="12" font-weight="500" fill="#6a7584">Status legend: established = exact analytic result; stress-tested = deterministic/fixed-seed synthetic check; open = evidence class not yet supplied by the repository.</text>
</svg>'''

def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    (FIGURES / "research_iii_measurement_architecture_v16_v55.svg").write_text(
        ARCHITECTURE + "\n", encoding="utf-8"
    )
    (FIGURES / "research_iii_uncertainty_propagation_v16_v55.svg").write_text(
        UNCERTAINTY + "\n", encoding="utf-8"
    )
    (FIGURES / "research_iii_validation_maturity_matrix.svg").write_text(
        MATURITY + "\n", encoding="utf-8"
    )

if __name__ == "__main__":
    main()
