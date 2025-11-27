'use client';

import { motion } from 'motion/react';

const features = [
  'Lead Management',
  'Sales Automation',
  'AI Assistant (Zia)',
  'Workflow Automation',
  'Omnichannel Communication',
];

export const FeatureChips = () => {
  return (
    <div className="flex flex-wrap gap-3 justify-center max-w-2xl mx-auto">
      {features.map((feature, index) => (
        <motion.div
          key={feature}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: index * 0.1, duration: 0.5 }}
          className="px-4 py-2 bg-blue-50 text-blue-700 rounded-full text-sm font-medium border border-blue-200 hover:bg-blue-100 transition-colors"
        >
          {feature}
        </motion.div>
      ))}
    </div>
  );
};
