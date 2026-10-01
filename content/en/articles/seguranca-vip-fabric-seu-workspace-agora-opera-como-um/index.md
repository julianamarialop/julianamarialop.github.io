---
title: "VIP Security in Fabric: your workspace now runs like an international airport"
slug: "vip-security-in-fabric-your-workspace-now-runs-like-an-international-airport"
date: 2025-05-12T16:15:00Z
summary: "Picture a large, modern airport with VIP lounges, strict protocols and exclusive tunnels for boarding and arrivals. Now picture that this airport is your Microsoft Fabric workspace."
tags: ["Microsoft Fabric", "Security"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/seguran%C3%A7a-vip-fabric-seu-workspace-agora-opera-como-um-lopes-20yff"
cover:
  image: cover.jpg
  alt: "VIP Security in Fabric: your workspace now runs like an international airport"
  relative: true
---

Picture a large, modern airport with VIP lounges, strict protocols and exclusive tunnels for boarding and arrivals. Now picture that this airport is your Microsoft Fabric workspace.

Starting in June 2025, [Microsoft Fabric](https://www.linkedin.com/company/microsoft-fabric-world/) gets two networking features, enabled by default, that bring exactly this level of security and control: **workspace-level Private Links** and **Outbound Access Protection**. Both are already available in Preview, and both are designed to protect your data with the same rigor as an international terminal.

---

### Private Links: the VIP entry tunnel

With the new Private Links, administrators can create private connections between their Azure virtual networks and Fabric workspaces. In other words, data now arrives through an exclusive tunnel, reserved only for trusted networks.

It's like giving your passengers a separate entrance with no access to the public concourse. No crowds, no unnecessary exposure. You decide who gets to land in your environment and you block every other kind of external access.

This feature lets the workspace run isolated from the public internet, which significantly reduces the risk of exposure or intrusion.

Setup is simple: go to "Advanced networking" and adjust the inbound rules at the workspace level.

---

### Outbound Access Protection: boarding only with a ticket

Just as airports strictly control who leaves, now Fabric does too. With Outbound Access Protection, no outbound connection is allowed from the workspace unless a **Managed Private Endpoint** is configured.

Think of it as boarding control. Your data can only leave the terminal if it holds an authorized, registered ticket. Without one, it doesn't board.

This measure helps prevent data exfiltration, whether accidental or intentional, and ensures that only approved paths out of the environment are used. The protection even extends to internal Fabric services, such as Spark notebooks.

To turn it on, just open "Workspace settings", go to "Network security" and select the option to block public outbound access.

---

### Central administration: your control tower

All of these features can be managed centrally by tenant administrators, who now have a dedicated section called "Advanced networking" in the Fabric admin portal.

From there, you can standardize security rules across the whole organization, enabling or disabling features according to internal policies. Since they come enabled by default, workspace administrators can apply them right away.

---

### Conclusion: an environment with international-grade security

With these two new features, Fabric stops being just a data platform and becomes an environment with real enterprise security standards.

By controlling both what comes in and what goes out, you turn your workspace into a VIP airport: with flows that are protected, traceable and fully under your control.

It's time to take command of the tower and make sure your data flies safely.
