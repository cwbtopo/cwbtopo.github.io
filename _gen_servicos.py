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
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=AW-18455722365"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'AW-18455722365');
    </script>
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
    <link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..800&family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet">
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
                <li><a href="index.html#servicos" class="nav-link">Serviços</a></li>
                <li><a href="sondagem-spt.html" class="nav-link">Sondagem SPT</a></li>
                <li><a href="index.html#projetos" class="nav-link">Projetos</a></li>
                <li><a href="index.html#sobre" class="nav-link">Sobre</a></li>
                <li><a href="index.html#contato" class="nav-link">Contato</a></li>
                <li class="nav-cta"><a href="#" class="btn btn-primary btn-sm" data-wa="header">Orçamento no WhatsApp</a></li>
            </ul>
            <button class="nav-toggle" aria-label="Abrir menu" aria-expanded="false">
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

            __GALERIA_SECTION__

            <div class="detalhe-conteudo">
                __CONTEUDO__

                <div class="detalhe-cta">
                    <h2>Precisa deste serviço?</h2>
                    <p>Solicite um orçamento sem compromisso. Atendemos Paraná, Santa Catarina e São Paulo.</p>
                    <a href="#" class="btn btn-primary" data-wa="cta">Pedir orçamento no WhatsApp</a>
                    <a href="index.html#contato" class="btn btn-ghost">Enviar mensagem</a>
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
                    <p>Topografia, georreferenciamento e investigação geotécnica desde 2020.</p>
                    <p>Curitiba, PR. Atendemos Paraná, Santa Catarina e São Paulo.</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 CWB Topografia. Todos os direitos reservados.</p>
            </div>
        </div>
    </footer>

    <script src="js/whatsapp.js"></script>
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
    {
        "slug": "pericia",
        "title": "Perícia Topográfica",
        "tagline": "Perícia técnica em divisas, áreas e conflitos de propriedade",
        "desc": "Perícia topográfica judicial e extrajudicial: levantamento de divisas, conferência de áreas, laudos e pareceres técnicos para conflitos de propriedade e processos judiciais. CWB Topografia, Paraná, Santa Catarina e São Paulo.",
        "keywords": "perícia topográfica, perícia judicial topografia, conflito de divisas, conferência de área, laudo pericial, assistente técnico, parecer técnico topografia, perito topógrafo Curitiba, CWB Topografia",
        "imgs": [],
        "blocos": [
            {"h2": "O serviço", "p": [
                "A <strong>perícia topográfica</strong> esclarece tecnicamente questões de divisas, áreas e localização de imóveis em processos judiciais e extrajudiciais. Atuamos como peritos ou assistentes técnicos, produzindo levantamentos, laudos e pareceres que dão base à decisão.",
            ]},
            {"h2": "O que entregamos", "ul": [
                "Levantamento topográfico das divisas em discussão;",
                "Confrontação entre títulos, matrículas e a situação de campo;",
                "Conferência de áreas e identificação de sobreposições;",
                "Laudo pericial e parecer técnico;",
                "Atuação como assistente técnico das partes.",
            ]},
            {"h2": "Aplicações", "ul": [
                "Ações de divisão, demarcação e reivindicatórias;",
                "Conflitos de divisa entre propriedades;",
                "Sobreposição de áreas e erros de matrícula;",
                "Apoio técnico a advogados e ao juízo.",
            ]},
        ],
    },
    {
        "slug": "ccir",
        "title": "CCIR",
        "tagline": "Certificado de Cadastro de Imóvel Rural junto ao INCRA",
        "desc": "Emissão e regularização do CCIR (Certificado de Cadastro de Imóvel Rural) junto ao INCRA: atualização cadastral, correção de dados e apoio à regularidade do imóvel rural. CWB Topografia.",
        "keywords": "CCIR, certificado de cadastro de imóvel rural, INCRA, cadastro rural, regularização CCIR, atualização cadastral imóvel rural, CWB Topografia",
        "imgs": [],
        "blocos": [
            {"h2": "O serviço", "p": [
                "O <strong>CCIR</strong> (Certificado de Cadastro de Imóvel Rural) é o documento emitido pelo INCRA que comprova a regularidade cadastral do imóvel rural e é exigido para venda, desmembramento, arrendamento e financiamento. Auxiliamos na emissão, atualização e correção das informações cadastrais.",
            ]},
            {"h2": "O que entregamos", "ul": [
                "Análise e atualização do cadastro do imóvel no INCRA;",
                "Correção de área, titularidade e demais dados;",
                "Apoio à emissão do CCIR;",
                "Compatibilização com o georreferenciamento (SIGEF);",
                "Orientação sobre a regularidade do imóvel rural.",
            ]},
            {"h2": "Aplicações", "ul": [
                "Venda, doação e partilha de imóveis rurais;",
                "Desmembramento e remembramento de glebas;",
                "Financiamento e crédito rural;",
                "Regularização cadastral junto ao INCRA.",
            ]},
        ],
    },
    {
        "slug": "car",
        "title": "CAR — Cadastro Ambiental Rural",
        "tagline": "Registro ambiental obrigatório dos imóveis rurais",
        "desc": "Elaboração do CAR (Cadastro Ambiental Rural): mapeamento de APP, Reserva Legal e uso do solo, com inscrição no SICAR para regularidade ambiental do imóvel rural. CWB Topografia, Paraná e região Sul.",
        "keywords": "CAR, cadastro ambiental rural, SICAR, APP, reserva legal, regularização ambiental, mapeamento de uso do solo, georreferenciamento ambiental, CWB Topografia",
        "imgs": [],
        "blocos": [
            {"h2": "O serviço", "p": [
                "O <strong>CAR</strong> (Cadastro Ambiental Rural) é o registro eletrônico obrigatório para todos os imóveis rurais, integrando as informações ambientais da propriedade no SICAR. Fazemos o mapeamento das áreas e a inscrição completa do imóvel.",
            ]},
            {"h2": "O que entregamos", "ul": [
                "Mapeamento de Áreas de Preservação Permanente (APP);",
                "Delimitação da Reserva Legal;",
                "Levantamento das áreas de uso consolidado e remanescentes de vegetação;",
                "Inscrição e retificação do imóvel no SICAR;",
                "Apoio à adequação ambiental da propriedade.",
            ]},
            {"h2": "Aplicações", "ul": [
                "Regularidade ambiental obrigatória do imóvel rural;",
                "Acesso a crédito e licenciamento;",
                "Programas de regularização ambiental (PRA);",
                "Adequação ao Código Florestal.",
            ]},
        ],
    },
    {
        "slug": "usucapiao",
        "title": "Usucapião Extrajudicial",
        "tagline": "Documentação técnica para reconhecimento da propriedade em cartório",
        "desc": "Apoio técnico ao usucapião extrajudicial: planta e memorial descritivo georreferenciados, assinados por profissional habilitado, para reconhecimento da posse diretamente no cartório. CWB Topografia.",
        "keywords": "usucapião extrajudicial, planta e memorial usucapião, georreferenciamento usucapião, ata notarial, reconhecimento de posse, regularização de propriedade cartório, CWB Topografia",
        "imgs": [],
        "blocos": [
            {"h2": "O serviço", "p": [
                "O <strong>usucapião extrajudicial</strong> permite reconhecer a propriedade de um imóvel diretamente no cartório, sem ação judicial, desde que apresentada a documentação técnica adequada. Elaboramos a planta e o memorial descritivo georreferenciados, assinados por profissional habilitado, peça essencial do processo.",
            ]},
            {"h2": "O que entregamos", "ul": [
                "Levantamento topográfico do imóvel;",
                "Planta e memorial descritivo georreferenciados;",
                "Anotação de Responsabilidade Técnica (ART);",
                "Identificação e descrição dos confrontantes;",
                "Documentação técnica para o tabelionato e o cartório de registro.",
            ]},
            {"h2": "Aplicações", "ul": [
                "Imóveis ocupados sem escritura ou registro;",
                "Regularização de posse de longa data;",
                "Imóveis urbanos e rurais;",
                "Reconhecimento da propriedade em cartório.",
            ]},
        ],
    },
    {
        "slug": "prad",
        "title": "PRAD — Plano de Recuperação de Áreas Degradadas",
        "tagline": "Diagnóstico e plano técnico para recuperação ambiental",
        "desc": "Elaboração de PRAD (Plano de Recuperação de Áreas Degradadas): diagnóstico, mapeamento da área e definição das ações de recuperação ambiental para atender exigências de órgãos ambientais. CWB Topografia.",
        "keywords": "PRAD, plano de recuperação de áreas degradadas, recuperação ambiental, APP degradada, condicionante ambiental, reflorestamento, diagnóstico ambiental, CWB Topografia",
        "imgs": [],
        "blocos": [
            {"h2": "O serviço", "p": [
                "O <strong>PRAD</strong> (Plano de Recuperação de Áreas Degradadas) reúne o diagnóstico e o conjunto de ações necessárias para recuperar áreas alteradas ou degradadas, sendo frequentemente exigido como condicionante por órgãos ambientais. Realizamos o levantamento, o diagnóstico e a elaboração técnica do plano.",
            ]},
            {"h2": "O que entregamos", "ul": [
                "Levantamento e mapeamento da área degradada;",
                "Diagnóstico ambiental da situação atual;",
                "Definição das técnicas e etapas de recuperação;",
                "Cronograma e indicadores de monitoramento;",
                "Documentação técnica para o órgão ambiental.",
            ]},
            {"h2": "Aplicações", "ul": [
                "Atendimento a condicionantes de licenciamento;",
                "Recuperação de APP e Reserva Legal;",
                "Áreas afetadas por obras ou atividades;",
                "Compensação e regularização ambiental.",
            ]},
        ],
    },
    {
        "slug": "avaliacao-imoveis",
        "title": "Avaliação de Imóveis",
        "tagline": "Laudos de avaliação conforme a norma ABNT NBR 14653",
        "desc": "Avaliação de imóveis urbanos e rurais com laudos técnicos conforme a norma ABNT NBR 14653, para fins de venda, garantia, partilha, desapropriação e processos judiciais. CWB Topografia.",
        "keywords": "avaliação de imóveis, laudo de avaliação, NBR 14653, valor de mercado, avaliação imóvel rural, avaliação imóvel urbano, laudo técnico imobiliário, desapropriação, CWB Topografia",
        "imgs": [],
        "badge": "Conforme a norma ABNT NBR 14653",
        "blocos": [
            {"h2": "O serviço", "p": [
                "A <strong>avaliação de imóveis</strong> determina, de forma técnica e fundamentada, o valor de mercado de propriedades urbanas e rurais. Emitimos laudos conforme a norma <strong>ABNT NBR 14653</strong>, com metodologia reconhecida e aceita por instituições, cartórios e pelo Poder Judiciário.",
            ]},
            {"h2": "O que entregamos", "ul": [
                "Vistoria e caracterização do imóvel;",
                "Pesquisa de mercado e tratamento dos dados;",
                "Definição do valor com metodologia da NBR 14653;",
                "Laudo de avaliação fundamentado;",
                "Anotação de Responsabilidade Técnica (ART).",
            ]},
            {"h2": "Aplicações", "ul": [
                "Compra, venda e garantia de imóveis;",
                "Partilha, inventário e divisão de bens;",
                "Desapropriação e processos judiciais;",
                "Decisões de investimento e gestão patrimonial.",
            ]},
        ],
    },
]


def build(svc):
    url = f"{BASE_URL}/{svc['slug']}.html"
    imgs = svc.get("imgs", [])
    if imgs:
        ogimg = f"{BASE_URL}/images/servicos/{imgs[0][0]}"
        galeria_section = (
            '<div class="spt-galeria">\n'
            f'                {galeria(imgs)}\n'
            '            </div>'
        )
    else:
        ogimg = f"{BASE_URL}/images/logo.jpg"
        galeria_section = ""
    badge = f'<span class="detalhe-norma">{escape(svc["badge"])}</span>' if svc.get("badge") else ""
    html = (PAGE
            .replace("__TITLE__", escape(svc["title"]))
            .replace("__TAGLINE__", escape(svc["tagline"]))
            .replace("__DESC__", escape(svc["desc"]))
            .replace("__KEYWORDS__", escape(svc["keywords"]))
            .replace("__URL__", url)
            .replace("__OGIMG__", ogimg)
            .replace("__BADGE__", badge)
            .replace("__GALERIA_SECTION__", galeria_section)
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
