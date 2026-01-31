"use client";

import { useState, useEffect } from "react";
import { ShieldCheck, Lock, AlertTriangle, Activity, MapPin, Terminal } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

export default function SentinelDashboard() {
  const [status, setStatus] = useState("SECURE"); // SECURE or LOCKED
  const [logs, setLogs] = useState<string[]>([]);
  const [scannedCount, setScannedCount] = useState(1420);

  // Poll the backend for status updates
  useEffect(() => {
    const interval = setInterval(async () => {
      try {
        // We check the status of our "victim" user
        const res = await fetch("http://localhost:8000/status/user_404");
        const data = await res.json();
        
        if (data.status === "LOCKED" && status !== "LOCKED") {
          setStatus("LOCKED");
          addLog("CRITICAL THREAT DETECTED: User_404");
          addLog("SENTINEL AGENT: Initiating Lockdown Protocol...");
          addLog("ACTION: Session Revoked. IP Blocked.");
        }
        
        // Simulator effect: Increment scanned count
        setScannedCount(prev => prev + Math.floor(Math.random() * 5));
      } catch (e) {
        console.error("Backend offline?");
      }
    }, 2000); // Check every 2 seconds

    return () => clearInterval(interval);
  }, [status]);

  const addLog = (msg: string) => {
    setLogs(prev => [`[${new Date().toLocaleTimeString()}] ${msg}`, ...prev].slice(0, 8));
  };

  return (
    <div className={`min-h-screen transition-colors duration-500 ${status === "LOCKED" ? "bg-red-950" : "bg-slate-950"} text-slate-200 font-mono overflow-hidden`}>
      
      {/* HEADER */}
      <header className="p-6 border-b border-white/10 flex justify-between items-center bg-black/20 backdrop-blur">
        <div className="flex items-center gap-3">
          <ShieldCheck className={`w-8 h-8 ${status === "LOCKED" ? "text-red-500" : "text-emerald-400"}`} />
          <h1 className="text-2xl font-bold tracking-widest">SENTINEL<span className="text-emerald-500">X</span> // SOC ENFORCER</h1>
        </div>
        <div className="flex gap-4 text-sm">
          <div className="flex items-center gap-2 px-3 py-1 rounded bg-white/5">
            <Activity className="w-4 h-4 text-blue-400" />
            <span>Traffic: {scannedCount} req/s</span>
          </div>
          <div className="flex items-center gap-2 px-3 py-1 rounded bg-white/5">
            <div className={`w-2 h-2 rounded-full ${status === "LOCKED" ? "bg-red-500 animate-ping" : "bg-emerald-500"}`} />
            <span>System: {status}</span>
          </div>
        </div>
      </header>

      {/* MAIN CONTENT */}
      <main className="p-8 grid grid-cols-1 md:grid-cols-2 gap-8 max-w-7xl mx-auto">
        
        {/* LEFT COLUMN: LIVE MAP & STATUS */}
        <div className="space-y-8">
          {/* LOCKDOWN OVERLAY */}
          <AnimatePresence>
            {status === "LOCKED" && (
              <motion.div 
                initial={{ scale: 0.8, opacity: 0 }}
                animate={{ scale: 1, opacity: 1 }}
                className="bg-red-600/20 border border-red-500/50 p-8 rounded-xl backdrop-blur-md relative overflow-hidden"
              >
                <div className="absolute inset-0 bg-red-500/10 animate-pulse" />
                <div className="relative z-10 flex flex-col items-center text-center">
                  <Lock className="w-24 h-24 text-red-500 mb-4" />
                  <h2 className="text-4xl font-black text-white mb-2">THREAT CONTAINED</h2>
                  <p className="text-red-200 text-lg">AI AGENT ENFORCED LOCKDOWN</p>
                  <div className="mt-6 text-left w-full bg-black/40 p-4 rounded text-sm">
                    <p>TARGET: <span className="text-white font-bold">user_404</span></p>
                    <p>REASON: <span className="text-white font-bold">Impossible Travel (Russia)</span></p>
                    <p>ACTION: <span className="text-red-400 font-bold">REVOKED & BLOCKED</span></p>
                  </div>
                </div>
              </motion.div>
            )}
          </AnimatePresence>

          {status === "SECURE" && (
            <div className="bg-emerald-900/10 border border-emerald-500/30 p-8 rounded-xl h-64 flex items-center justify-center">
              <div className="text-center space-y-4">
                <ShieldCheck className="w-20 h-20 text-emerald-500 mx-auto opacity-50" />
                <p className="text-emerald-400 tracking-widest text-lg">ACTIVE MONITORING</p>
                <p className="text-xs text-slate-500">Scanning Identity Logs...</p>
              </div>
            </div>
          )}
        </div>

        {/* RIGHT COLUMN: TERMINAL LOGS */}
        <div className="bg-black/80 border border-white/10 rounded-xl p-4 font-mono text-xs md:text-sm h-125 flex flex-col">
          <div className="flex items-center gap-2 mb-4 text-slate-400 border-b border-white/10 pb-2">
            <Terminal className="w-4 h-4" />
            <span>AGENT_LOG_STREAM</span>
          </div>
          <div className="flex-1 overflow-y-auto space-y-2">
             {logs.length === 0 && <span className="text-slate-600 italic">Waiting for events...</span>}
             {logs.map((log, i) => (
               <motion.div 
                 key={i}
                 initial={{ x: -10, opacity: 0 }}
                 animate={{ x: 0, opacity: 1 }}
                 className={`${log.includes("CRITICAL") ? "text-red-400 font-bold bg-red-900/20" : "text-emerald-400/80"}`}
               >
                 {log}
               </motion.div>
             ))}
          </div>
        </div>

      </main>
    </div>
  );
}