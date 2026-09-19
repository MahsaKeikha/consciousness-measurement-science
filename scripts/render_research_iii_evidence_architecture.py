from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "docs" / "figures" / "research_iii_evidence_architecture.svg"

SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000">
  <defs>
    <marker id="arrow" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 Z" fill="#637083"/>
    </marker>
    <linearGradient id="headerBand" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#f5f8fc"/>
      <stop offset="100%" stop-color="#fbfcfe"/>
    </linearGradient>
  </defs>
  <rect width="1600" height="1000" fill="#ffffff"/>
  <rect x="0" y="0" width="1600" height="150" fill="url(#headerBand)"/>
  <text x="78" y="48" font-family="Arial, Helvetica, sans-serif" font-size="13" font-weight="700" letter-spacing="1.4" fill="#3156a3">RESEARCH III  |  MEASUREMENT SCIENCE ARCHITECTURE</text>
  <text x="78" y="88" font-family="Arial, Helvetica, sans-serif" font-size="34" font-weight="700" fill="#172236">From physical evidence to claims that survive identifiability, inference, replication, and transport</text>
  <text x="78" y="121" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#5f6e82">The program advances only when each layer passes its own failure test. No layer, by itself, turns an electromagnetic statistic into a direct measure of consciousness.</text>
  <rect x="1260" y="42" width="250" height="34" rx="17" fill="#eef3fb" stroke="#c8d5ea"/>
  <text x="1385" y="64" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#3156a3">ANALYTIC + SYNTHETIC VALIDATION</text>

  <text x="78" y="194" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" letter-spacing="1.2" fill="#687588">EVIDENCE PATH</text>
  <line x1="150" y1="360" x2="1450" y2="360" stroke="#c7d0dc" stroke-width="2"/>

  <rect x="80" y="230" width="165" height="250" rx="18" fill="#f5f8fb" stroke="#bfd0df" stroke-width="2"/>
  <text x="105" y="262" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315b78">01  V16-V20</text>
  <text x="105" y="300" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#173b63">Field organization</text>
  <text x="105" y="329" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">Ask whether structure</text>
  <text x="105" y="350" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">survives scale and</text>
  <text x="105" y="371" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">confound removal.</text>
  <line x1="105" y1="399" x2="220" y2="399" stroke="#d7e1ea"/>
  <text x="105" y="425" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315b78">FAILURE GATE</text>
  <text x="105" y="448" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="#5d6a7b">Gain or common-mode</text>
  <text x="105" y="467" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="#5d6a7b">artifact explains signal.</text>

  <rect x="262" y="230" width="165" height="250" rx="18" fill="#f7f9f4" stroke="#c7d4be" stroke-width="2"/>
  <text x="287" y="262" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#506b3f">02  V21-V25</text>
  <text x="287" y="300" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#3d5b32">Source identity</text>
  <text x="287" y="329" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">Expose null spaces,</text>
  <text x="287" y="350" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">regularization, and</text>
  <text x="287" y="371" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">forward-model error.</text>
  <line x1="287" y1="399" x2="402" y2="399" stroke="#d9e2d3"/>
  <text x="287" y="425" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#506b3f">FAILURE GATE</text>
  <text x="287" y="448" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="#5d6a7b">Different sources produce</text>
  <text x="287" y="467" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="#5d6a7b">indistinguishable sensors.</text>

  <rect x="444" y="230" width="165" height="250" rx="18" fill="#fbf7f9" stroke="#dcc9d3" stroke-width="2"/>
  <text x="469" y="262" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#7b435c">03  V26-V30</text>
  <text x="469" y="300" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#6a3f57">Resolution limits</text>
  <text x="469" y="329" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">Quantify leakage,</text>
  <text x="469" y="350" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">correlated noise,</text>
  <text x="469" y="371" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">aliasing, amplification.</text>
  <line x1="469" y1="399" x2="584" y2="399" stroke="#e6d7df"/>
  <text x="469" y="425" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#7b435c">FAILURE GATE</text>
  <text x="469" y="448" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="#5d6a7b">Acquisition geometry cannot</text>
  <text x="469" y="467" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="#5d6a7b">resolve declared distinction.</text>

  <rect x="626" y="230" width="165" height="250" rx="18" fill="#f5f8fb" stroke="#bfd0df" stroke-width="2"/>
  <text x="651" y="262" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315b78">04  V31-V35</text>
  <text x="651" y="300" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#173b63">Design quality</text>
  <text x="651" y="329" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">Optimize spatial</text>
  <text x="651" y="350" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">specificity, nuisance</text>
  <text x="651" y="371" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">rejection, robustness.</text>
  <line x1="651" y1="399" x2="766" y2="399" stroke="#d7e1ea"/>
  <text x="651" y="425" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315b78">FAILURE GATE</text>
  <text x="651" y="448" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="#5d6a7b">Sensor design is redundant</text>
  <text x="651" y="467" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="#5d6a7b">or nuisance-dominated.</text>

  <rect x="808" y="230" width="165" height="250" rx="18" fill="#f7f9f4" stroke="#c7d4be" stroke-width="2"/>
  <text x="833" y="262" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#506b3f">05  V36-V40</text>
  <text x="833" y="300" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#3d5b32">Finite inference</text>
  <text x="833" y="329" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">Calibrate variance,</text>
  <text x="833" y="350" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">coverage, discrimination,</text>
  <text x="833" y="371" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">multiplicity.</text>
  <line x1="833" y1="399" x2="948" y2="399" stroke="#d9e2d3"/>
  <text x="833" y="425" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#506b3f">FAILURE GATE</text>
  <text x="833" y="448" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="#5d6a7b">Nominal uncertainty does</text>
  <text x="833" y="467" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="#5d6a7b">not match realized error.</text>

  <rect x="990" y="230" width="165" height="250" rx="18" fill="#fbf7f9" stroke="#dcc9d3" stroke-width="2"/>
  <text x="1015" y="262" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#7b435c">06  V41-V45</text>
  <text x="1015" y="300" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#6a3f57">Selection safety</text>
  <text x="1015" y="329" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">Control family-wise</text>
  <text x="1015" y="350" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">error and isolate</text>
  <text x="1015" y="371" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">confirmation data.</text>
  <line x1="1015" y1="399" x2="1130" y2="399" stroke="#e6d7df"/>
  <text x="1015" y="425" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#7b435c">FAILURE GATE</text>
  <text x="1015" y="448" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="#5d6a7b">Discovery reuse collapses</text>
  <text x="1015" y="467" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="#5d6a7b">post-selection validity.</text>

  <rect x="1172" y="230" width="165" height="250" rx="18" fill="#f5f8fb" stroke="#bfd0df" stroke-width="2"/>
  <text x="1197" y="262" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315b78">07  V46-V50</text>
  <text x="1197" y="300" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#173b63">Replication</text>
  <text x="1197" y="329" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">Test heterogeneity,</text>
  <text x="1197" y="350" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">site influence, and</text>
  <text x="1197" y="371" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">replicability.</text>
  <line x1="1197" y1="399" x2="1312" y2="399" stroke="#d7e1ea"/>
  <text x="1197" y="425" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#315b78">FAILURE GATE</text>
  <text x="1197" y="448" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="#5d6a7b">One site dominates or</text>
  <text x="1197" y="467" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="#5d6a7b">effects fail to replicate.</text>

  <rect x="1354" y="230" width="165" height="250" rx="18" fill="#f7f9f4" stroke="#c7d4be" stroke-width="2"/>
  <text x="1379" y="262" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#506b3f">08  V51-V55</text>
  <text x="1379" y="300" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#3d5b32">Transport</text>
  <text x="1379" y="329" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">Stress coordinates,</text>
  <text x="1379" y="350" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">hardware, populations,</text>
  <text x="1379" y="371" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">distribution shift.</text>
  <line x1="1379" y1="399" x2="1494" y2="399" stroke="#d9e2d3"/>
  <text x="1379" y="425" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#506b3f">FAILURE GATE</text>
  <text x="1379" y="448" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="#5d6a7b">Measurement relation fails</text>
  <text x="1379" y="467" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="#5d6a7b">under domain change.</text>

  <line x1="245" y1="360" x2="262" y2="360" stroke="#637083" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="427" y1="360" x2="444" y2="360" stroke="#637083" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="609" y1="360" x2="626" y2="360" stroke="#637083" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="791" y1="360" x2="808" y2="360" stroke="#637083" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="973" y1="360" x2="990" y2="360" stroke="#637083" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="1155" y1="360" x2="1172" y2="360" stroke="#637083" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="1337" y1="360" x2="1354" y2="360" stroke="#637083" stroke-width="2" marker-end="url(#arrow)"/>

  <text x="78" y="545" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" letter-spacing="1.2" fill="#687588">CLAIM DISCIPLINE</text>
  <rect x="80" y="575" width="1440" height="136" rx="18" fill="#fbfcfe" stroke="#d8dee8" stroke-width="1.5"/>
  <text x="118" y="615" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="700" fill="#3156a3">PHYSICAL OBSERVABLE</text>
  <text x="118" y="647" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700" fill="#172236">Measured electromagnetic structure</text>
  <text x="118" y="678" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#5f6e82">Field, sensor, source-model, and statistical quantities are evidence channels.</text>

  <line x1="495" y1="645" x2="590" y2="645" stroke="#637083" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="610" y="615" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="700" fill="#506b3f">VALIDATED RELATION</text>
  <text x="610" y="647" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700" fill="#172236">Identified, calibrated, and transport-tested link</text>
  <text x="610" y="678" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#5f6e82">The relation must survive the declared assumptions and failure gates above.</text>

  <line x1="1055" y1="645" x2="1150" y2="645" stroke="#637083" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="1170" y="615" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="700" fill="#7b435c">CLAIM CEILING</text>
  <text x="1170" y="647" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700" fill="#172236">No direct consciousness claim yet</text>
  <text x="1170" y="678" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#5f6e82">Human empirical target validation remains a separate scientific requirement.</text>

  <text x="78" y="768" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" letter-spacing="1.2" fill="#687588">HOW TO READ THE RESULT FIGURES</text>
  <rect x="80" y="798" width="1440" height="116" rx="18" fill="#f6f8fb" stroke="#d4dce7"/>
  <text x="118" y="838" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="700" fill="#3156a3">QUESTION</text>
  <text x="118" y="868" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">What failure mode is this stage designed to expose?</text>
  <text x="495" y="838" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="700" fill="#506b3f">EVIDENCE</text>
  <text x="495" y="868" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">What analytic law, deterministic construction, or fixed-seed simulation is plotted?</text>
  <text x="1000" y="838" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="700" fill="#7b435c">INTERPRETATION</text>
  <text x="1000" y="868" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#4f5e72">What does the result establish, and what does it explicitly not establish?</text>

  <line x1="80" y1="950" x2="1520" y2="950" stroke="#d8dee8"/>
  <text x="80" y="978" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="#6a7684">Research III is a measurement-science validation program. The architecture guides empirical design; it is not evidence that consciousness has already been directly measured.</text>
</svg>
"""


def main() -> None:
    FIGURE.parent.mkdir(parents=True, exist_ok=True)
    FIGURE.write_text(SVG, encoding="utf-8")


if __name__ == "__main__":
    main()
