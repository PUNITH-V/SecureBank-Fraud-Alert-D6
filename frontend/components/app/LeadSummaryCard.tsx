'use client';

import { motion } from 'motion/react';
import { useState, useEffect } from 'react';

interface LeadData {
  name?: string;
  company?: string;
  email?: string;
  role?: string;
  use_case?: string;
  team_size?: string;
  timeline?: string;
  timestamp?: string;
}

export const LeadSummaryCard = () => {
  const [leadData, setLeadData] = useState<LeadData | null>(null);
  const [showToast, setShowToast] = useState(false);

  useEffect(() => {
    // Poll for lead_data.json every 2 seconds
    const interval = setInterval(async () => {
      try {
        const response = await fetch('/api/lead-data');
        if (response.ok) {
          const data = await response.json();
          if (data && Object.keys(data).length > 0) {
            setLeadData(data);
            setShowToast(true);
            setTimeout(() => setShowToast(false), 5000);
            clearInterval(interval);
          }
        }
      } catch (error) {
        // Silently fail - file might not exist yet
      }
    }, 2000);

    return () => clearInterval(interval);
  }, []);

  const downloadJSON = () => {
    if (!leadData) return;
    
    const dataStr = JSON.stringify(leadData, null, 2);
    const dataBlob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(dataBlob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `lead_${leadData.name?.replace(/\s+/g, '_') || 'data'}.json`;
    link.click();
    URL.revokeObjectURL(url);
  };

  if (!leadData) return null;

  return (
    <>
      {/* Toast Notification */}
      {showToast && (
        <motion.div
          initial={{ opacity: 0, y: -50 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -50 }}
          className="fixed top-5 right-5 bg-green-500 text-white px-6 py-3 rounded-lg shadow-xl z-50 flex items-center gap-3"
        >
          <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
          </svg>
          <span className="font-semibold">Lead Captured Successfully!</span>
        </motion.div>
      )}

      {/* Lead Summary Card */}
      <motion.div
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.5 }}
        className="w-full max-w-2xl mx-auto mt-8 bg-white rounded-2xl shadow-2xl border border-gray-200 overflow-hidden"
      >
        <div className="bg-gradient-to-r from-blue-600 to-blue-700 px-6 py-4">
          <h3 className="text-xl font-bold text-white flex items-center gap-2">
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            Lead Information Captured
          </h3>
        </div>

        <div className="p-6 space-y-4">
          {leadData.name && (
            <div className="flex items-start gap-3">
              <span className="text-gray-500 font-medium min-w-[120px]">Name:</span>
              <span className="text-gray-900 font-semibold">{leadData.name}</span>
            </div>
          )}
          
          {leadData.company && (
            <div className="flex items-start gap-3">
              <span className="text-gray-500 font-medium min-w-[120px]">Company:</span>
              <span className="text-gray-900 font-semibold">{leadData.company}</span>
            </div>
          )}
          
          {leadData.email && (
            <div className="flex items-start gap-3">
              <span className="text-gray-500 font-medium min-w-[120px]">Email:</span>
              <span className="text-blue-600 font-semibold">{leadData.email}</span>
            </div>
          )}
          
          {leadData.role && (
            <div className="flex items-start gap-3">
              <span className="text-gray-500 font-medium min-w-[120px]">Role:</span>
              <span className="text-gray-900">{leadData.role}</span>
            </div>
          )}
          
          {leadData.use_case && (
            <div className="flex items-start gap-3">
              <span className="text-gray-500 font-medium min-w-[120px]">Use Case:</span>
              <span className="text-gray-900">{leadData.use_case}</span>
            </div>
          )}
          
          {leadData.team_size && (
            <div className="flex items-start gap-3">
              <span className="text-gray-500 font-medium min-w-[120px]">Team Size:</span>
              <span className="text-gray-900">{leadData.team_size}</span>
            </div>
          )}
          
          {leadData.timeline && (
            <div className="flex items-start gap-3">
              <span className="text-gray-500 font-medium min-w-[120px]">Timeline:</span>
              <span className="text-gray-900">{leadData.timeline}</span>
            </div>
          )}

          <div className="pt-4 border-t border-gray-200">
            <button
              onClick={downloadJSON}
              className="w-full bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 text-white font-semibold py-3 px-6 rounded-lg transition-all shadow-lg hover:shadow-xl flex items-center justify-center gap-2"
            >
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
              Download Lead JSON
            </button>
          </div>
        </div>
      </motion.div>
    </>
  );
};
