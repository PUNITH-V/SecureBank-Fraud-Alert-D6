'use client';

import { motion } from 'motion/react';

const faqTopics = [
  { icon: '💰', label: 'Pricing Plans', color: 'bg-green-50 text-green-700 border-green-200' },
  { icon: '🎁', label: 'Free Trial', color: 'bg-purple-50 text-purple-700 border-purple-200' },
  { icon: '⚡', label: 'Features', color: 'bg-blue-50 text-blue-700 border-blue-200' },
  { icon: '🔗', label: 'Integrations', color: 'bg-orange-50 text-orange-700 border-orange-200' },
  { icon: '🎯', label: 'Use Cases', color: 'bg-pink-50 text-pink-700 border-pink-200' },
];

export const QuickFAQSection = () => {
  return (
    <div className="w-full max-w-4xl mx-auto">
      <motion.h3
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.3 }}
        className="text-2xl font-bold text-gray-800 mb-6 text-center"
      >
        What You Can Ask
      </motion.h3>
      
      <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
        {faqTopics.map((topic, index) => (
          <motion.div
            key={topic.label}
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.4 + index * 0.1, duration: 0.4 }}
            className={`${topic.color} p-4 rounded-xl border text-center hover:shadow-lg transition-all cursor-default`}
          >
            <div className="text-3xl mb-2">{topic.icon}</div>
            <div className="text-sm font-semibold">{topic.label}</div>
          </motion.div>
        ))}
      </div>
    </div>
  );
};
