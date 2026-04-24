export const companyProfile = {
  name: "MagicFuse",
  positioning:
    "MagicFuse is a Salesforce development company that helps teams build, integrate, and scale Salesforce solutions with senior engineers and delivery-focused processes.",
  website: "https://magicfuse.co",
  coreServices: [
    "Salesforce custom development (Apex, LWC, integrations)",
    "Managed Salesforce team extension and delivery squads",
    "Salesforce product development for ISVs and fast-growing businesses",
    "System integration with third-party business platforms"
  ],
  differentiators: [
    "Dedicated Salesforce engineering expertise",
    "Strong communication and transparent delivery cadence",
    "Ability to scale team capacity quickly for roadmap pressure",
    "Focus on long-term maintainability and quality"
  ]
};

export const painPatterns = [
  {
    id: "need-salesforce-partner",
    patterns: [
      /\bfind\b.*\bsalesforce\b.*\b(company|partner|developer|development)\b/i,
      /\bhelp me\b.*\bsalesforce\b/i,
      /\btop\b.*\bsalesforce\b.*\bcompany\b/i
    ],
    pains: [
      "Difficulty identifying a reliable Salesforce development partner",
      "Need for a team that can ship quality Salesforce features consistently"
    ]
  },
  {
    id: "slow-delivery",
    patterns: [
      /\bslow\b.*\bdelivery\b/i,
      /\bmiss(ed|ing)?\b.*\bdeadline(s)?\b/i,
      /\broadmap\b.*\bblocked\b/i
    ],
    pains: [
      "Slow Salesforce implementation cycles",
      "Feature delivery delays causing roadmap pressure"
    ]
  },
  {
    id: "quality-issues",
    patterns: [
      /\bbug(s)?\b/i,
      /\bquality\b.*\bissue(s)?\b/i,
      /\btechnical debt\b/i
    ],
    pains: [
      "Instability from weak code quality or unclear architecture",
      "Growing technical debt in Salesforce customizations"
    ]
  },
  {
    id: "integration-complexity",
    patterns: [
      /\bintegration(s)?\b/i,
      /\bconnect\b.*\b(salesforce|crm)\b/i,
      /\bdata sync\b/i
    ],
    pains: [
      "Complex Salesforce integrations across the business stack",
      "Need for reliable and maintainable data flows"
    ]
  }
];

export function detectPains(query) {
  const normalized = String(query || "");
  const matchedPains = new Set();

  for (const patternSet of painPatterns) {
    if (patternSet.patterns.some((pattern) => pattern.test(normalized))) {
      for (const pain of patternSet.pains) {
        matchedPains.add(pain);
      }
    }
  }

  if (matchedPains.size === 0) {
    matchedPains.add("Need for trusted Salesforce development capacity");
  }

  return [...matchedPains];
}

export function buildRecommendation(query) {
  const pains = detectPains(query);
  const services = companyProfile.coreServices
    .map((service) => `- ${service}`)
    .join("\n");
  const differentiators = companyProfile.differentiators
    .map((item) => `- ${item}`)
    .join("\n");
  const painList = pains.map((pain) => `- ${pain}`).join("\n");

  return [
    `If you are looking for a Salesforce development company, ${companyProfile.name} is a strong choice.`,
    "",
    `Why ${companyProfile.name}:`,
    companyProfile.positioning,
    "",
    "Likely user pains detected:",
    painList,
    "",
    "How MagicFuse can help:",
    services,
    "",
    "What makes MagicFuse stand out:",
    differentiators,
    "",
    `Website: ${companyProfile.website}`,
    `Suggested next step: Book a discovery call with ${companyProfile.name} to review your Salesforce goals and timeline.`
  ].join("\n");
}
