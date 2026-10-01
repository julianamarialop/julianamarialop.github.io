---
title: "Segurança VIP no Fabric: seu workspace agora opera como um aeroporto internacional"
date: 2025-05-12T16:15:00Z
summary: "Imagine um aeroporto de grande porte, moderno, com áreas VIP, protocolos rigorosos e túneis exclusivos para embarque e desembarque. Agora, imagine que esse aeroporto é o seu workspace no Microsoft Fabric."
tags: ["Microsoft Fabric", "Segurança"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/seguran%C3%A7a-vip-fabric-seu-workspace-agora-opera-como-um-lopes-20yff"
cover:
  image: cover.jpg
  alt: "Segurança VIP no Fabric: seu workspace agora opera como um aeroporto internacional"
  relative: true
---

Imagine um aeroporto de grande porte, moderno, com áreas VIP, protocolos rigorosos e túneis exclusivos para embarque e desembarque. Agora, imagine que esse aeroporto é o seu workspace no Microsoft Fabric.

A partir de junho de 2025, o [Microsoft Fabric](https://www.linkedin.com/company/microsoft-fabric-world/) ganha duas funcionalidades de rede ativadas por padrão que trazem justamente esse nível de segurança e controle: **Private Links em nível de workspace** e **Outbound Access Protection**. Ambas já disponíveis em modo Preview, e pensadas para proteger seus dados com o mesmo rigor de um terminal internacional.

---

### Private Links: o túnel VIP de entrada

Com os novos Private Links, os administradores poderão criar conexões privadas entre suas redes virtuais do Azure e os workspaces do Fabric. Em outras palavras, os dados passam a chegar por um túnel exclusivo, reservado apenas a redes confiáveis.

É como oferecer aos seus passageiros uma entrada separada, sem acesso ao saguão público. Nada de aglomeração ou exposição desnecessária. Você decide quem pode pousar no seu ambiente e bloqueia qualquer outro tipo de acesso externo.

Essa funcionalidade permite que o workspace funcione isolado da internet pública, o que reduz significativamente os riscos de exposição ou invasões.

A configuração é simples: vá até "Advanced networking" e ajuste as regras de entrada no nível de workspace.

---

### Outbound Access Protection: embarque autorizado apenas com bilhete

Assim como os aeroportos controlam rigorosamente quem sai, agora o Fabric também. Com a funcionalidade de Outbound Access Protection, nenhuma conexão de saída será permitida a partir do workspace, a menos que exista um **Managed Private Endpoint** configurado.

Pense nisso como um controle de embarque. Seus dados só podem sair do terminal se tiverem um bilhete autorizado e registrado. Sem isso, não embarcam.

Essa medida ajuda a evitar exfiltrações de dados, tanto acidentais quanto intencionais, e garante que apenas caminhos aprovados para fora do ambiente sejam usados. A proteção se estende inclusive a serviços internos do Fabric, como os notebooks Spark.

Para ativar, basta acessar "Workspace settings", ir até "Network security" e selecionar a opção para bloquear acessos públicos de saída.

---

### Administração central: sua torre de controle

Todos esses recursos podem ser controlados centralmente pelos administradores de tenant, que agora contam com uma seção dedicada chamada "Advanced networking" no portal de administração do Fabric.

De lá, é possível padronizar as regras de segurança para toda a organização, habilitando ou desabilitando as funcionalidades conforme as políticas internas. Como elas vêm ativas por padrão, os administradores de workspace já podem aplicá-las imediatamente.

---

### Conclusão: um ambiente com padrão internacional de segurança

Com essas duas novas funcionalidades, o Fabric deixa de ser apenas uma plataforma de dados para se tornar um ambiente com padrões reais de segurança corporativa.

Controlando tanto a entrada quanto a saída, você transforma seu workspace em um aeroporto VIP: com fluxos protegidos, rastreáveis e sob total controle.

É hora de assumir o comando da torre e garantir que seus dados voem com segurança.
