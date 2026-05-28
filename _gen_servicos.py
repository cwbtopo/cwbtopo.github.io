# -*- coding: utf-8 -*-
"""Gera páginas de descrição de serviço para o site CWB Topografia.

Cada serviço vira um arquivo HTML na raiz (ex.: pavimentacao.html), usando o
mesmo cabeçalho, rodapé e CSS do site. A página de Sondagem SPT é mantida à
parte (sondagem-spt.html), pois tem fotos e conteúdo próprios.

Uso:
    python _gen_servicos.py
"""
from html import escape

BASE_URL = "https://cwbtopo.github.io"

PAGE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="__DESC__">
    <meta name="robots" content="index,follow">
    <meta name="keywords" content="__KEYWORDS__">
    <meta name="author" content="CWB Topografia">
    <meta name="geo.region" content="BR-PR">
    <meta name="geo.placename" content="Curitiba, Paraná, Brasil">
    <link rel="canonical" href="__URL__">
    <link rel="icon" type="image/svg+xml" href="favicon.svg">

    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="__TITLE__ | CWB Topografia">
    <meta property="og:description" content="__DESC__">
    <meta property="og:url" content="__URL__">
    <meta property="og:locale" content="pt_BR">
    <meta property="og:site_name" content="CWB Topografia">
    <meta property="og:image" content="__OGIMG__">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="__TITLE__ | CWB Topografia">
    <meta name="twitter:description" content="__DESC__">
    <meta name="twitter:image" content="__OGIMG__">

    <title>__TITLE__ | CWB Topografia</title>

    <!-- JSON-LD: Service -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Service",
      "serviceType": "__TITLE__",
      "name": "__TITLE__",
      "description": "__DESC__",
      "provider": {
        "@type": ["LocalBusiness", "ProfessionalService"],
        "name": "CWB Topografia",
        "url": "https://cwbtopo.github.io/",
        "telephone": "+55-41-99772-7085",
        "areaServed": ["Paraná", "Santa Catarina", "São Paulo"]
      },
      "areaServed": [
        {"@type": "AdministrativeArea", "name": "Paraná"},
        {"@type": "AdministrativeArea", "name": "Santa Catarina"},
        {"@type": "AdministrativeArea", "name": "São Paulo"}
      ]
    }
    </script>

    <!-- JSON-LD: Breadcrumb -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": "https://cwbtopo.github.io/"},
        {"@type": "ListItem", "position": 2, "name": "Serviços", "item": "https://cwbtopo.github.io/#servicos"},
        {"@type": "ListItem", "position": 3, "name": "__TITLE__", "item": "__URL__"}
      ]
    }
    </script>

    <link rel="stylesheet" href="css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&family=Open+Sans:wght@400;500;600&display=swap" rel="stylesheet">

    <style>
        .servico-detalhe {
            padding: calc(var(--spacing-4xl) + 60px) 0 var(--spacing-4xl);
            background: linear-gradient(180deg, var(--color-white) 0%, var(--color-light) 100%);
        }
        .detalhe-breadcrumb {
            font-size: 0.875rem;
            color: var(--color-gray-600);
            margin-bottom: var(--spacing-lg);
        }
        .detalhe-breadcrumb a { color: var(--color-primary); font-weight: 600; }
        .detalhe-header { max-width: 820px; margin: 0 auto var(--spacing-2xl); text-align: center; }
        .detalhe-header h1 { font-size: 2.5rem; color: var(--color-secondary); margin-bottom: var(--spacing-sm); }
        .detalhe-tagline { font-size: 1.125rem; color: var(--color-primary-dark); font-weight: 600; margin-bottom: var(--spacing-md); }
        .detalhe-norma {
            display: inline-block; background: var(--gradient-primary); color: var(--color-white);
            padding: 0.4rem 1.1rem; border-radius: var(--radius-xl); font-size: 0.875rem; font-weight: 600;
        }
        .spt-galeria {
            display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: var(--spacing-lg); margin: var(--spacing-2xl) 0;
        }
        .spt-galeria figure {
            margin: 0; border-radius: var(--radius-xl); overflow: hidden;
            box-shadow: var(--shadow-lg); background: var(--color-white);
        }
        .spt-galeria img {
            width: 100%; height: 320px; object-fit: cover; display: block;
            transition: transform var(--transition-slow);
        }
        .spt-galeria figure:hover img { transform: scale(1.05); }
        .spt-galeria figcaption {
            padding: var(--spacing-sm) var(--spacing-md); font-size: 0.875rem;
            color: var(--color-gray-600); text-align: center;
        }
        .detalhe-conteudo { max-width: 880px; margin: 0 auto; }
        .detalhe-conteudo h2 { font-size: 1.6rem; color: var(--color-primary-dark); margin: var(--spacing-2xl) 0 var(--spacing-md); }
        .detalhe-conteudo p { color: var(--color-gray-700); margin-bottom: var(--spacing-md); line-height: 1.8; }
        .detalhe-conteudo ul { list-style: none; margin-bottom: var(--spacing-md); }
        .detalhe-conteudo ul li {
            position: relative; padding-left: 1.75rem; margin-bottom: var(--spacing-sm);
            color: var(--color-gray-700); line-height: 1.7;
        }
        .detalhe-conteudo ul li::before {
            content: ''; position: absolute; left: 0; top: 0.55em; width: 9px; height: 9px;
            border-radius: 50%; background: var(--color-primary);
        }
        .detalhe-cta {
            text-align: center; margin-top: var(--spacing-2xl); padding: var(--spacing-2xl);
            background: var(--color-white); border-radius: var(--radius-xl); box-shadow: var(--shadow-lg);
        }
        .detalhe-cta h2 { margin-top: 0; }
        @media (max-width: 768px) {
            .spt-galeria img { height: 260px; }
            .detalhe-header h1 { font-size: 1.9rem; }
        }
    </style>
</head>
<body>
    <!-- Header / Navegação -->
    <header class="header">
        <nav class="nav container">
            <div class="logo">
                <a href="index.html" style="display:flex;align-items:center;text-decoration:none;color:inherit;">
                    <img src="images/logo.jpg" alt="CWB Topografia Logo" class="logo-img">
                    <span class="logo-text">CWB<span class="logo-accent">TOPOGRAFIA</span></span>
                </a>
            </div>
            <ul class="nav-menu">
                <li><a href="index.html#inicio" class="nav-link">Início</a></li>
                <li><a href="index.html#sobre" class="nav-link">Sobre</a></li>
                <li><a href="index.html#servicos" class="nav-link">Serviços</a></li>
                <li><a href="index.html#projetos" class="nav-link">Projetos</a></li>
                <li><a href="index.html#equipe" class="nav-link">Equipe</a></li>
                <li><a href="index.html#contato" class="nav-link">Contato</a></li>
            </ul>
            <button class="nav-toggle" aria-label="Toggle menu">
                <span class="hamburger"></span>
            </button>
        </nav>
    </header>

    <!-- Conteúdo do Serviço -->
    <section class="servico-detalhe">
        <div class="container">
            <nav class="detalhe-breadcrumb">
                <a href="index.html">Início</a> &rsaquo;
                <a href="index.html#servicos">Serviços</a> &rsaquo;
                <span>__TITLE__</span>
            </nav>

            <div class="detalhe-header">
                <h1>__TITLE__</h1>
                <p class="detalhe-tagline">__TAGLINE__</p>
                __BADGE__
            </div>

            <div class="spt-galeria">
                __GALERIA__
            </div>

            <div class="detalhe-conteudo">
                __CONTEUDO__

                <div class="detalhe-cta">
                    <h2>Precisa deste serviço?</h2>
                    <p>Solicite um orçamento sem compromisso. Atendemos Paraná, Santa Catarina e São Paulo.</p>
                    <a href="index.html#contato" class="btn btn-primary">Solicitar Orçamento</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-logo">
                    <img src="images/logo.jpg" alt="CWB Topografia Logo" class="footer-logo-img">
                    <span class="footer-logo-text">CWB<span class="logo-accent">TOPOGRAFIA</span></span>
                </div>
                <div class="footer-info">
                    <p>Desde 2020 oferecendo soluções em topografia e georreferenciamento.</p>
                    <p>Paraná | Santa Catarina | São Paulo</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 CWB Topografia. Todos os direitos reservados.</p>
            </div>
        </div>
    </footer>

    <script src="js/main.js"></script>
</body>
</html>
"""


def galeria(imgs):
    out = []
    for src, cap in imgs:
        out.append(
            '<figure>\n'
            f'                    <img src="images/servicos/{src}" alt="{escape(cap)}">\n'
            f'                    <figcaption>{escape(cap)}</figcaption>\n'
            '                </figure>'
        )
    return "\n                ".join(out)


def conteudo(blocos):
    parts = []
    for b in blocos:
        parts.append(f'<h2>{escape(b["h2"])}</h2>')
        for p in b.get("p", []):
            parts.append(f'<p>{p}</p>')
        if b.get("ul"):
            lis = "\n                    ".join(f'<li>{escape(li)}</li>' for li in b["ul"])
            parts.append(f'<ul>\n                    {lis}\n                </ul>')
    return "\n                ".join(parts)


SERVICES = [
    {
        "slug": "pavimentacao",
        "title": "Pavimentação",
        "tagline": "Levantamentos topográficos para projetos de pavimentação urbana e rodoviária",
        "desc": "Levantamentos topográficos para projetos de pavimentação com precisão milimétrica: perfis longitudinais, seções transversais, greide e cálculo de volumes de terraplenagem em Curitiba e todo o Paraná.",
        "keywords": "pavimentação topografia, levantamento para pavimentação, perfil longitudinal, seção transversal, greide, terraplenagem, cálculo de volume corte aterro, topografia rodoviária Curitiba, CWB Topografia",
        "imgs": [("pavimentacao.jpg", "Levantamento topográfico para projeto de pavimentação")],
        "blocos": [
            {"h2": "O serviço", "p": [
                "Realizamos os levantamentos topográficos que dão base aos projetos de <strong>pavimentação</strong> de vias urbanas, loteamentos e rodovias. A partir do levantamento planialtimétrico do eixo e das faixas de domínio, geramos as informações necessárias para o dimensionamento do greide, dos perfis e das seções de projeto.",
            ]},
            {"h2": "O que entregamos", "ul": [
                "Levantamento planialtimétrico cadastral da via e do entorno;",
                "Perfil longitudinal e seções transversais do eixo;",
                "Definição de greide e cotas de projeto;",
                "Cálculo de volumes de corte e aterro (terraplenagem);",
                "Locação e acompanhamento da obra de pavimentação.",
            ]},
            {"h2": "Aplicações", "ul": [
                "Pavimentação asfáltica e de concreto em vias urbanas;",
                "Implantação de ruas em loteamentos e condomínios;",
                "Recapeamento e duplicação de rodovias;",
                "Drenagem e infraestrutura viária.",
            ]},
        ],
    },
    {
        "slug": "controle-obra",
        "title": "Controle de Obra",
        "tagline": "Acompanhamento topográfico durante todas as fases da construção",
        "desc": "Controle topográfico de obra com locação de eixos, pilares e estruturas, verificação de cotas e monitoramento dimensional em todas as fases da construção. Atendimento em Curitiba, Paraná, Santa Catarina e São Paulo.",
        "keywords": "controle de obra topografia, locação de obra, locação de pilares, controle dimensional, monitoramento de recalque, as built de obra, topografia construção civil Curitiba, CWB Topografia",
        "imgs": [("controle-obra.jpg", "Controle topográfico em canteiro de obra")],
        "blocos": [
            {"h2": "O serviço", "p": [
                "O <strong>controle de obra</strong> garante que tudo seja construído exatamente como previsto em projeto. Acompanhamos a obra do início ao fim, fazendo a locação dos elementos estruturais e conferindo continuamente as cotas e o alinhamento das estruturas.",
            ]},
            {"h2": "O que entregamos", "ul": [
                "Locação de eixos, pilares, fundações e estruturas;",
                "Verificação de prumo, nível e alinhamento;",
                "Conferência de cotas de piso e lajes;",
                "Monitoramento de recalques e deslocamentos;",
                "Relatórios periódicos de acompanhamento.",
            ]},
            {"h2": "Aplicações", "ul": [
                "Edificações residenciais, comerciais e industriais;",
                "Obras de infraestrutura e estruturas de grande porte;",
                "Galpões logísticos e plantas industriais;",
                "Verificação de conformidade com o projeto executivo.",
            ]},
        ],
    },
    {
        "slug": "as-built",
        "title": "As Built",
        "tagline": "Documentação precisa do que foi efetivamente construído",
        "desc": "Levantamento As Built: documentação topográfica fiel do que foi efetivamente construído, com plantas e modelos atualizados da edificação ou infraestrutura. CWB Topografia, Curitiba e região Sul.",
        "keywords": "as built, levantamento as built, documentação do construído, planta as built, cadastro de redes, topografia as built Curitiba, CWB Topografia",
        "imgs": [("as-built.jpg", "Levantamento As Built da edificação")],
        "blocos": [
            {"h2": "O serviço", "p": [
                "O <strong>As Built</strong> (\"como construído\") registra com precisão a situação final de uma obra, que quase sempre apresenta diferenças em relação ao projeto original. Fazemos o levantamento do que foi efetivamente executado e entregamos a documentação atualizada da edificação ou da infraestrutura.",
            ]},
            {"h2": "O que entregamos", "ul": [
                "Levantamento dimensional do construído;",
                "Plantas, cortes e perfis atualizados;",
                "Cadastro de redes e instalações;",
                "Modelo 2D/3D fiel à realidade da obra;",
                "Documentação para regularização e manutenção.",
            ]},
            {"h2": "Aplicações", "ul": [
                "Regularização de edificações junto à prefeitura;",
                "Cadastro de redes de água, esgoto e drenagem;",
                "Base para reformas, ampliações e manutenção;",
                "Documentação final de obras de infraestrutura.",
            ]},
        ],
    },
    {
        "slug": "modelagem-ponte",
        "title": "Modelagem de Ponte",
        "tagline": "Levantamentos detalhados para projetos, inspeção e manutenção de pontes",
        "desc": "Modelagem de pontes com levantamento por drone e estação total, gerando modelos 3D, plantas e nuvens de pontos para projeto, inspeção e manutenção de obras de arte especiais. CWB Topografia.",
        "keywords": "modelagem de ponte, levantamento de ponte, inspeção de pontes, obras de arte especiais, modelo 3D ponte, levantamento aéreo ponte drone, topografia ponte Paraná, CWB Topografia",
        "imgs": [
            ("ponte-foto.jpg", "Modelagem topográfica de ponte"),
            ("ponte-aerea.jpg", "Levantamento aéreo da estrutura com drone"),
            ("ponte-planta.jpg", "Planta e modelo gerados a partir do levantamento"),
        ],
        "blocos": [
            {"h2": "O serviço", "p": [
                "Realizamos a <strong>modelagem de pontes</strong> e obras de arte especiais combinando levantamento aéreo com drone e medições com estação total e GNSS. O resultado é um modelo tridimensional preciso da estrutura, usado em projetos, inspeções e planos de manutenção.",
            ]},
            {"h2": "O que entregamos", "ul": [
                "Levantamento aéreo e terrestre da estrutura;",
                "Nuvem de pontos e modelo 3D da ponte;",
                "Plantas, cortes e perfis detalhados;",
                "Identificação geométrica de elementos estruturais;",
                "Base técnica para projetos de reforço e recuperação.",
            ]},
            {"h2": "Aplicações", "ul": [
                "Projetos de reforma, alargamento e duplicação;",
                "Inspeção e monitoramento estrutural;",
                "Planejamento de manutenção e recuperação;",
                "Documentação técnica de obras de arte especiais.",
            ]},
        ],
    },
    {
        "slug": "batimetria",
        "title": "Batimetria",
        "tagline": "Medição de profundidade de corpos d'água com equipamentos de última geração",
        "desc": "Batimetria para medição de profundidade de rios, lagos, reservatórios e áreas portuárias, com ecobatímetro integrado a GNSS para geração de modelos de fundo e cálculo de volumes. CWB Topografia.",
        "keywords": "batimetria, levantamento batimétrico, ecobatímetro, profundidade de rio, assoreamento, dragagem, volume de reservatório, batimetria GNSS, topografia subaquática Paraná, CWB Topografia",
        "imgs": [
            ("batimetria-drone.jpg", "Levantamento batimétrico em corpo d'água"),
            ("batimetria-gnss.jpg", "Batimetria integrada a posicionamento GNSS"),
        ],
        "blocos": [
            {"h2": "O serviço", "p": [
                "A <strong>batimetria</strong> mapeia o relevo do fundo de rios, lagos, reservatórios e áreas portuárias. Utilizamos ecobatímetro integrado a posicionamento GNSS de alta precisão, gerando o modelo digital do fundo e permitindo o cálculo preciso de volumes e profundidades.",
            ]},
            {"h2": "O que entregamos", "ul": [
                "Mapeamento de profundidade e relevo de fundo;",
                "Modelo digital do leito (MDT subaquático);",
                "Cálculo de volume de água e de sedimentos;",
                "Curvas batimétricas e seções transversais;",
                "Estudos de assoreamento e apoio à dragagem.",
            ]},
            {"h2": "Aplicações", "ul": [
                "Reservatórios, barragens e usinas hidrelétricas;",
                "Portos, canais e áreas de dragagem;",
                "Estudos de assoreamento e capacidade de reservatório;",
                "Projetos de travessias e obras hidráulicas.",
            ]},
        ],
    },
    {
        "slug": "lidar",
        "title": "LIDAR",
        "tagline": "Escaneamento a laser para levantamentos de alta densidade e precisão",
        "desc": "Levantamento LIDAR com drone para geração de nuvens de pontos de alta densidade, modelos digitais de terreno e superfície mesmo em áreas com vegetação. CWB Topografia, Curitiba e região Sul.",
        "keywords": "LIDAR, levantamento lidar drone, nuvem de pontos, modelo digital de terreno, MDT, MDS, escaneamento a laser, lidar topografia Paraná, mapeamento vegetação, CWB Topografia",
        "imgs": [("lidar-drone.jpg", "Levantamento LIDAR com drone")],
        "blocos": [
            {"h2": "O serviço", "p": [
                "A tecnologia <strong>LIDAR</strong> (escaneamento a laser) embarcada em drone captura milhões de pontos por segundo, gerando uma representação tridimensional extremamente detalhada do terreno. Sua grande vantagem é a capacidade de penetrar a vegetação e mapear o solo mesmo em áreas com cobertura vegetal densa.",
            ]},
            {"h2": "O que entregamos", "ul": [
                "Nuvem de pontos georreferenciada de alta densidade;",
                "Modelo Digital de Terreno (MDT) e de Superfície (MDS);",
                "Curvas de nível e mapeamento altimétrico;",
                "Mapeamento sob vegetação;",
                "Cálculo de volumes e análises topográficas.",
            ]},
            {"h2": "Aplicações", "ul": [
                "Áreas florestais e de vegetação densa;",
                "Projetos de infraestrutura, mineração e energia;",
                "Estudos de drenagem e modelagem hidrológica;",
                "Grandes áreas com necessidade de alta precisão.",
            ]},
        ],
    },
    {
        "slug": "reurb",
        "title": "REURB",
        "tagline": "Regularização Fundiária Urbana de núcleos urbanos informais",
        "desc": "REURB: Regularização Fundiária Urbana de núcleos informais, com levantamento topográfico, ortomosaico por drone e plantas para titulação das famílias conforme a Lei 13.465/2017. CWB Topografia.",
        "keywords": "REURB, regularização fundiária urbana, Lei 13.465/2017, ortomosaico drone, levantamento de núcleo urbano informal, titulação, planta de regularização, REURB Curitiba Paraná, CWB Topografia",
        "imgs": [
            ("reurb-ortomosaico.jpg", "Ortomosaico aéreo do núcleo urbano"),
            ("reurb-planta.jpg", "Planta de regularização fundiária"),
        ],
        "blocos": [
            {"h2": "O serviço", "p": [
                "A <strong>REURB</strong> (Regularização Fundiária Urbana), instituída pela Lei 13.465/2017, permite regularizar núcleos urbanos informais e dar segurança jurídica às famílias por meio da titulação dos imóveis. Fazemos toda a parte técnica de topografia e mapeamento que dá suporte ao processo.",
            ]},
            {"h2": "O que entregamos", "ul": [
                "Levantamento topográfico do núcleo urbano;",
                "Ortomosaico e mapeamento aéreo por drone;",
                "Plantas de parcelamento e individualização dos lotes;",
                "Memoriais descritivos das unidades;",
                "Documentação técnica para o processo de titulação.",
            ]},
            {"h2": "Aplicações", "ul": [
                "Regularização de loteamentos e ocupações urbanas;",
                "Programas habitacionais municipais e estaduais;",
                "Titulação de imóveis para famílias de baixa renda;",
                "Projetos como o \"Escritura na Mão\" e similares.",
            ]},
        ],
    },
    {
        "slug": "regularizacao-fundiaria",
        "title": "Regularização Fundiária",
        "tagline": "Legalização de imóveis rurais e urbanos junto aos órgãos competentes",
        "desc": "Regularização fundiária de imóveis rurais e urbanos: georreferenciamento, certificação no SIGEF/INCRA, retificação de área e documentação para legalização junto aos órgãos competentes. CWB Topografia.",
        "keywords": "regularização fundiária, georreferenciamento de imóvel rural, SIGEF, INCRA, certificação de imóvel, retificação de área, usucapião, regularização rural urbana Paraná, CWB Topografia",
        "imgs": [
            ("reurb-planta.jpg", "Planta para regularização fundiária"),
            ("reurb-ortomosaico.jpg", "Mapeamento aéreo da área a regularizar"),
        ],
        "blocos": [
            {"h2": "O serviço", "p": [
                "A <strong>regularização fundiária</strong> resolve pendências documentais e cartoriais de imóveis rurais e urbanos, garantindo a segurança jurídica da propriedade. Conduzimos o levantamento, o georreferenciamento e a documentação técnica necessária para a legalização junto ao cartório e aos órgãos competentes.",
            ]},
            {"h2": "O que entregamos", "ul": [
                "Georreferenciamento de imóvel rural e certificação no SIGEF/INCRA;",
                "Levantamento e retificação de área e de divisas;",
                "Plantas e memoriais descritivos;",
                "Apoio técnico a processos de usucapião extrajudicial;",
                "Documentação para registro em cartório.",
            ]},
            {"h2": "Aplicações", "ul": [
                "Imóveis rurais sem georreferenciamento;",
                "Retificação de área e correção de matrícula;",
                "Usucapião e inventários;",
                "Desmembramento, unificação e parcelamento de glebas.",
            ]},
        ],
    },
]


def build(svc):
    url = f"{BASE_URL}/{svc['slug']}.html"
    ogimg = f"{BASE_URL}/images/servicos/{svc['imgs'][0][0]}"
    badge = f'<span class="detalhe-norma">{escape(svc["badge"])}</span>' if svc.get("badge") else ""
    html = (PAGE
            .replace("__TITLE__", escape(svc["title"]))
            .replace("__TAGLINE__", escape(svc["tagline"]))
            .replace("__DESC__", escape(svc["desc"]))
            .replace("__KEYWORDS__", escape(svc["keywords"]))
            .replace("__URL__", url)
            .replace("__OGIMG__", ogimg)
            .replace("__BADGE__", badge)
            .replace("__GALERIA__", galeria(svc["imgs"]))
            .replace("__CONTEUDO__", conteudo(svc["blocos"])))
    return html


def main():
    for svc in SERVICES:
        out = f"{svc['slug']}.html"
        with open(out, "w", encoding="utf-8") as f:
            f.write(build(svc))
        print("gerado:", out)


if __name__ == "__main__":
    main()
