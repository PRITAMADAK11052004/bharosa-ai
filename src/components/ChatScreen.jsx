import { useState, useRef, useEffect } from 'react';
import { MessageCircle, BookOpen, Brain, Settings, Plus, Mic, FileText, Camera, Home, Zap, Shield, Send, Upload, Trash2, ChevronDown } from 'lucide-react';

const BharosaApp = () => {
  const [activeTab, setActiveTab] = useState('home');

  const getGreeting = () => {
    const h = new Date().getHours();
    return h < 12 ? 'Good morning' : h < 17 ? 'Good afternoon' : 'Good evening';
  };

  const HomeScreen = () => (
    <div style={{ flex: 1, overflowY: 'auto', padding: '24px 20px 100px' }}>

      {/* Animated greeting */}
      <div style={{ marginBottom: '28px' }}>
        <h1 style={{ margin: '0 0 4px', fontSize: '28px', fontWeight: '800', color: '#f1f5f9', lineHeight: 1.2 }}>
          {getGreeting()} 🌅
        </h1>
        <h1 style={{ margin: '0 0 10px', fontSize: '22px', fontWeight: '700', lineHeight: 1.35,
          background: 'linear-gradient(90deg, #fb923c, #f97316, #ea580c)',
          WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>
          Aap kaise hain aaj? ✨
        </h1>
        <p style={{ margin: '0 0 5px', fontSize: '14px', color: '#94a3b8', lineHeight: 1.6 }}>
          Koi baat ho, koi sawaal ho — hum yahan hain.
        </p>
        <p style={{ margin: 0, fontSize: '13px', color: '#475569', fontStyle: 'italic' }}>
          No judgement, bas apnapan. 💛
        </p>
      </div>

      {/* Quick Actions */}
      <div style={{ display: 'flex', gap: '10px', marginBottom: '32px', overflowX: 'auto', paddingBottom: '4px' }}>
        {[
          { label: 'Ask anything', icon: <MessageCircle size={13} />, color: '#f97316' },
          { label: 'Scan document', icon: <Camera size={13} />, color: '#a78bfa' },
          { label: 'Voice note', icon: <Mic size={13} />, color: '#34d399' },
          { label: 'Deep think', icon: <Brain size={13} />, color: '#60a5fa' },
        ].map((a, i) => (
          <button key={i} onClick={() => setActiveTab('chat')} style={{
            display: 'flex', alignItems: 'center', gap: '7px',
            padding: '10px 18px', borderRadius: '24px', fontSize: '13px',
            background: 'rgba(255,255,255,0.06)',
            border: `1px solid rgba(255,255,255,0.1)`,
            color: a.color, cursor: 'pointer', whiteSpace: 'nowrap', flexShrink: 0,
            fontWeight: '500'
          }}>
            {a.icon} {a.label}
          </button>
        ))}
      </div>

      {/* Insights */}
      <p style={{ fontSize: '11px', fontWeight: '700', letterSpacing: '0.12em', color: '#475569', marginBottom: '14px' }}>
        TODAY'S INSIGHTS
      </p>

      {[
        {
          tag: 'MACHINE LEARNING', tagColor: '#a78bfa', tagBg: 'rgba(124,58,237,0.18)',
          title: 'Transformer Architecture Summary',
          desc: 'Your ML Lecture 7 covers multi-head attention, positional encoding, and the encoder-decoder stack in depth.',
          border: 'rgba(124,58,237,0.25)'
        },
        {
          tag: 'OS CONCEPTS', tagColor: '#34d399', tagBg: 'rgba(5,150,105,0.18)',
          title: 'Semaphore vs Monitor Comparison',
          desc: '3 key distinctions found across your OS notes — relevant to upcoming exam topics.',
          border: 'rgba(5,150,105,0.25)'
        },
      ].map((ins, i) => (
        <div key={i} style={{
          background: 'rgba(255,255,255,0.04)',
          border: `1px solid ${ins.border}`,
          borderRadius: '20px', padding: '20px', marginBottom: '14px',
          cursor: 'pointer', transition: 'all 0.2s'
        }}>
          <span style={{
            fontSize: '10px', fontWeight: '700', letterSpacing: '0.08em',
            background: ins.tagBg, color: ins.tagColor,
            padding: '4px 12px', borderRadius: '20px'
          }}>{ins.tag}</span>
          <h3 style={{ margin: '12px 0 8px', fontSize: '17px', fontWeight: '700', color: '#f1f5f9' }}>
            {ins.title}
          </h3>
          <p style={{ margin: 0, fontSize: '13px', color: '#64748b', lineHeight: '1.6' }}>
            {ins.desc}
          </p>
        </div>
      ))}

      {/* Memory Health */}
      <p style={{ fontSize: '11px', fontWeight: '700', letterSpacing: '0.12em', color: '#475569', margin: '28px 0 14px' }}>
        MEMORY HEALTH
      </p>
      <div style={{
        background: 'rgba(255,255,255,0.04)',
        border: '1px solid rgba(34,211,238,0.2)',
        borderRadius: '20px', padding: '20px', marginBottom: '28px'
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '14px' }}>
          <div>
            <p style={{ margin: 0, fontSize: '17px', fontWeight: '700', color: '#22d3ee' }}>Fully Indexed</p>
            <p style={{ margin: '4px 0 0', fontSize: '13px', color: '#64748b' }}>5 of 6 files processed</p>
          </div>
          <span style={{
            fontSize: '32px', fontWeight: '800',
            background: 'linear-gradient(135deg, #22d3ee, #818cf8)',
            WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent'
          }}>92%</span>
        </div>
        <div style={{ height: '8px', background: 'rgba(255,255,255,0.06)', borderRadius: '4px', marginBottom: '14px', overflow: 'hidden' }}>
          <div style={{
            width: '92%', height: '100%',
            background: 'linear-gradient(90deg, #6366f1, #22d3ee)',
            borderRadius: '4px',
            animation: 'growBar 1.5s ease-out'
          }} />
        </div>
        <p style={{ margin: 0, fontSize: '12px', color: '#475569' }}>
          🔒 All data local • 0 cloud uploads • Last sync: charging
        </p>
      </div>

      {/* Recent Activity */}
      <p style={{ fontSize: '11px', fontWeight: '700', letterSpacing: '0.12em', color: '#475569', marginBottom: '14px' }}>
        RECENT ACTIVITY
      </p>
      {[
        { name: 'OS Notes - Semaphores.pdf', time: 'Today', size: '2.1 MB', icon: '📄', color: 'rgba(99,102,241,0.15)' },
        { name: 'ML Lecture 7 - Transformers...', time: 'Yesterday', size: '4.8 MB', icon: '📄', color: 'rgba(249,115,22,0.15)' },
        { name: 'Architecture Diagram.png', time: '2 days ago', size: '890 KB', icon: '🖼️', color: 'rgba(52,211,153,0.15)' },
      ].map((file, i) => (
        <div key={i} style={{
          display: 'flex', alignItems: 'center', gap: '14px',
          background: 'rgba(255,255,255,0.03)',
          border: '1px solid rgba(255,255,255,0.07)',
          borderRadius: '16px', padding: '14px 16px', marginBottom: '10px'
        }}>
          <div style={{
            width: '44px', height: '44px', borderRadius: '12px',
            background: file.color,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            fontSize: '20px', flexShrink: 0
          }}>
            {file.icon}
          </div>
          <div style={{ flex: 1, minWidth: 0 }}>
            <p style={{ margin: 0, fontSize: '14px', fontWeight: '600', color: '#e2e8f0', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
              {file.name}
            </p>
            <p style={{ margin: '3px 0 0', fontSize: '12px', color: '#475569' }}>
              {file.time} · {file.size}
            </p>
          </div>
          <button onClick={() => setActiveTab('chat')} style={{
            padding: '7px 16px', borderRadius: '20px', fontSize: '12px',
            background: 'rgba(34,211,238,0.1)',
            border: '1px solid rgba(34,211,238,0.25)',
            color: '#22d3ee', cursor: 'pointer', flexShrink: 0, fontWeight: '500'
          }}>
            Continue
          </button>
        </div>
      ))}
    </div>
  );

  // ─── UPGRADED CHAT SCREEN ────────────────────────────────────────────────────
  const ChatScreen = () => {
    const [messages, setMessages] = useState([
      { id: 1, text: "Hello! I'm Bharosa AI — your personal offline cognitive companion. How can I help you today?", isUser: false }
    ]);
    const [input, setInput] = useState('');
    const [mode, setMode] = useState('Deep Reasoning');
    const [isThinking, setIsThinking] = useState(false);
    const [uploadedFile, setUploadedFile] = useState(null);
    const messagesEndRef = useRef(null);

    useEffect(() => {
      messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [messages]);

    const sendMessage = () => {
      if (!input.trim() || isThinking) return;
      const q = input;
      setMessages(prev => [...prev, { id: Date.now(), text: q, isUser: true }]);
      setInput('');
      setIsThinking(true);
      const tid = 'think' + Date.now();
      setMessages(prev => [...prev, { id: tid, isThinking: true, isUser: false, text: '' }]);

      const delay = 1000 + Math.random() * 900;
      const sendMessage = async () => {
  if (!input.trim() || isThinking) return;

  const q = input;

  setMessages(prev => [...prev, { id: Date.now(), text: q, isUser: true }]);
  setInput('');
  setIsThinking(true);

  const tid = 'think' + Date.now();
  setMessages(prev => [...prev, { id: tid, isThinking: true, isUser: false }]);

  try {
    const res = await fetch("http://192.168.0.12:8000/query", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        query: q
      })
    });

    const data = await res.json();

    setMessages(prev => prev.filter(m => m.id !== tid));

    setMessages(prev => [...prev, {
      id: Date.now(),
      isUser: false,
      text: data.answer,
      sources: data.sources || []
    }]);

  } catch (err) {
    setMessages(prev => prev.filter(m => m.id !== tid));
    setMessages(prev => [...prev, {
      id: Date.now(),
      isUser: false,
      text: "❌ Error connecting to backend"
    }]);
  }

  setIsThinking(false);
}}

    const clearChat = () => {
      setMessages([{ id: 1, text: "Hello! I'm Bharosa AI — your personal offline cognitive companion. How can I help you today?", isUser: false }]);
    };

    const modeColors = {
      'Normal': '#64748b',
      'Deep Reasoning': '#f97316',
      'Summarize': '#a78bfa',
      'Compare': '#34d399',
    };

    return (
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>

        {/* ── Chat Header (upgraded) ── */}
        <div style={{
          padding: '12px 16px',
          borderBottom: '1px solid rgba(255,255,255,0.06)',
          background: 'rgba(8,13,24,0.8)',
          backdropFilter: 'blur(12px)',
        }}>
          {/* Row 1: avatar + name + clear */}
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '10px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
              <div style={{
                width: '38px', height: '38px', borderRadius: '50%',
                background: 'linear-gradient(135deg, #f97316, #ea580c)',
                display: 'flex', alignItems: 'center', justifyContent: 'center',
                boxShadow: '0 0 14px rgba(249,115,22,0.4)', flexShrink: 0
              }}>
                <Brain size={17} color="white" />
              </div>
              <div>
                <p style={{ margin: 0, fontSize: '15px', fontWeight: '700', color: '#f1f5f9' }}>Bharosa</p>
                <p style={{ margin: 0, fontSize: '11px', color: '#22d3ee' }}>● Offline Mode Active</p>
              </div>
            </div>

            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              {uploadedFile && (
                <span style={{
                  fontSize: '11px', color: '#f97316', padding: '4px 10px',
                  background: 'rgba(249,115,22,0.1)', borderRadius: '20px',
                  border: '1px solid rgba(249,115,22,0.2)',
                  maxWidth: '100px', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap'
                }}>
                  📄 {uploadedFile}
                </span>
              )}
              <button onClick={clearChat} style={{
                background: 'transparent', border: '1px solid rgba(239,68,68,0.25)',
                color: '#f87171', padding: '6px 8px', borderRadius: '10px', cursor: 'pointer',
                display: 'flex', alignItems: 'center'
              }}>
                <Trash2 size={13} />
              </button>
            </div>
          </div>

          {/* Row 2: Mode selector pills */}
          <div style={{ display: 'flex', gap: '7px', overflowX: 'auto', paddingBottom: '2px' }}>
            {['Normal', 'Deep Reasoning', 'Summarize', 'Compare'].map(m => (
              <button key={m} onClick={() => setMode(m)} style={{
                padding: '6px 14px', borderRadius: '20px', fontSize: '12px', fontWeight: '600',
                border: `1px solid ${mode === m ? modeColors[m] : 'rgba(255,255,255,0.08)'}`,
                background: mode === m ? `${modeColors[m]}18` : 'transparent',
                color: mode === m ? modeColors[m] : '#475569',
                cursor: 'pointer', whiteSpace: 'nowrap', flexShrink: 0,
                transition: 'all 0.18s'
              }}>
                {m === 'Deep Reasoning' ? '🧠 ' : m === 'Summarize' ? '📋 ' : m === 'Compare' ? '⚖️ ' : '💬 '}{m}
              </button>
            ))}
          </div>
        </div>

        {/* ── Messages ── */}
        <div style={{ flex: 1, overflowY: 'auto', padding: '20px 16px', display: 'flex', flexDirection: 'column', gap: '20px' }}>
          {messages.map(msg => (
            <div key={msg.id} style={{
              display: 'flex',
              justifyContent: msg.isUser ? 'flex-end' : 'flex-start',
              alignItems: 'flex-end', gap: '10px'
            }}>
              {/* AI avatar */}
              {!msg.isUser && (
                <div style={{
                  width: '32px', height: '32px', borderRadius: '50%',
                  background: 'linear-gradient(135deg, #f97316, #ea580c)',
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  flexShrink: 0, boxShadow: '0 0 10px rgba(249,115,22,0.35)'
                }}>
                  <Brain size={14} color="white" />
                </div>
              )}

              {/* Bubble */}
              <div style={{
                maxWidth: '76%',
                background: msg.isUser
                  ? 'linear-gradient(135deg, #ea580c, #f97316)'
                  : 'rgba(255,255,255,0.05)',
                border: msg.isUser ? 'none' : '1px solid rgba(255,255,255,0.09)',
                borderRadius: msg.isUser ? '20px 20px 4px 20px' : '20px 20px 20px 4px',
                padding: '14px 18px',
                boxShadow: msg.isUser ? '0 4px 20px rgba(234,88,12,0.28)' : 'none',
                transition: 'transform 0.15s',
              }}>
                {msg.isThinking ? (
                  <div style={{ display: 'flex', gap: '5px', alignItems: 'center', padding: '2px 0' }}>
                    <span style={{ fontSize: '12px', color: '#94a3b8', marginRight: '4px' }}>Thinking</span>
                    {[0,1,2].map(i => (
                      <div key={i} style={{
                        width: '6px', height: '6px', borderRadius: '50%',
                        background: '#f97316',
                        animation: `bounce 1s ${i * 0.2}s infinite ease-in-out`
                      }} />
                    ))}
                  </div>
                ) : (
                  <>
                    {!msg.isUser && (
                      <div style={{ display: 'flex', alignItems: 'center', gap: '6px', marginBottom: '6px' }}>
                        <p style={{ margin: 0, fontSize: '10px', color: '#f97316', fontWeight: '700', letterSpacing: '0.1em' }}>
                          BHAROSA
                        </p>
                        <span style={{
                          fontSize: '9px', fontWeight: '700', letterSpacing: '0.06em',
                          color: modeColors[mode], background: `${modeColors[mode]}15`,
                          padding: '2px 8px', borderRadius: '20px',
                          border: `1px solid ${modeColors[mode]}30`
                        }}>{mode.toUpperCase()}</span>
                      </div>
                    )}
                    <p style={{ margin: 0, fontSize: '14px', lineHeight: '1.7', color: msg.isUser ? 'white' : '#e2e8f0' }}>
                      {msg.text}
                    </p>

                    {/* Source Citations */}
                    {msg.sources && (
                      <div style={{ marginTop: '12px', paddingTop: '10px', borderTop: '1px solid rgba(255,255,255,0.08)' }}>
                        <p style={{ margin: '0 0 6px', fontSize: '10px', color: '#64748b', fontWeight: '700', letterSpacing: '0.08em' }}>
                          SOURCES
                        </p>
                        {msg.sources.map((s, i) => (
                          <div key={i} style={{
                            display: 'flex', alignItems: 'center', justifyContent: 'space-between',
                            fontSize: '11px', color: '#f97316',
                            background: 'rgba(249,115,22,0.08)',
                            border: '1px solid rgba(249,115,22,0.15)',
                            padding: '6px 11px', borderRadius: '10px', marginTop: '5px',
                            gap: '6px'
                          }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '5px', minWidth: 0 }}>
                              <FileText size={10} style={{ flexShrink: 0 }} />
                              <span style={{ overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{s.file}</span>
                            </div>
                            <span style={{
                              color: '#22d3ee', fontWeight: '600', flexShrink: 0,
                              background: 'rgba(34,211,238,0.1)', padding: '2px 8px', borderRadius: '8px'
                            }}>
                              p.{s.page}
                            </span>
                          </div>
                        ))}
                      </div>
                    )}
                  </>
                )}
              </div>

              {/* User avatar */}
              {msg.isUser && (
                <div style={{
                  width: '32px', height: '32px', borderRadius: '50%',
                  background: 'linear-gradient(135deg, #6366f1, #818cf8)',
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  flexShrink: 0, fontWeight: '700', fontSize: '13px', color: 'white'
                }}>
                  A
                </div>
              )}
            </div>
          ))}
          <div ref={messagesEndRef} />
        </div>

        {/* ── Input Area ── */}
        <div style={{ padding: '12px 16px 16px', borderTop: '1px solid rgba(255,255,255,0.06)' }}>
          <div style={{
            display: 'flex', gap: '8px', alignItems: 'center',
            background: 'rgba(255,255,255,0.05)',
            border: `1px solid ${isThinking ? 'rgba(249,115,22,0.15)' : 'rgba(249,115,22,0.28)'}`,
            borderRadius: '16px', padding: '8px 8px 8px 14px',
            boxShadow: '0 0 20px rgba(249,115,22,0.05)',
            transition: 'border-color 0.2s'
          }}>
            <label style={{ cursor: 'pointer', color: '#f97316', padding: '4px', flexShrink: 0 }}>
              <Upload size={17} />
              <input type="file" accept=".pdf" style={{ display: 'none' }}
                onChange={e => { const f = e.target.files?.[0]; if (f) setUploadedFile(f.name); }} />
            </label>
            <input
              value={input}
              onChange={e => setInput(e.target.value)}
              onKeyPress={e => e.key === 'Enter' && sendMessage()}
              placeholder="Ask anything about your documents..."
              disabled={isThinking}
              style={{
                flex: 1, background: 'transparent', border: 'none',
                outline: 'none', color: '#e2e8f0', fontSize: '14px'
              }}
            />
            <button style={{ background: 'transparent', border: 'none', color: '#f97316', cursor: 'pointer', padding: '4px', flexShrink: 0 }}>
              <Mic size={17} />
            </button>
            <button onClick={sendMessage} disabled={!input.trim() || isThinking} style={{
              background: input.trim() && !isThinking
                ? 'linear-gradient(135deg, #ea580c, #f97316)'
                : 'rgba(255,255,255,0.07)',
              border: 'none', borderRadius: '10px', padding: '9px 13px',
              cursor: input.trim() && !isThinking ? 'pointer' : 'not-allowed',
              color: 'white', display: 'flex', alignItems: 'center',
              flexShrink: 0,
              boxShadow: input.trim() && !isThinking ? '0 0 15px rgba(249,115,22,0.3)' : 'none',
              transition: 'all 0.2s'
            }}>
              <Send size={15} />
            </button>
          </div>
          <p style={{ textAlign: 'center', fontSize: '11px', color: '#1e293b', marginTop: '8px' }}>
            🔒 100% Private • All processing happens locally
          </p>
        </div>
      </div>
    );
  };

  const Placeholder = ({ label, icon }) => (
    <div style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: '14px', color: '#334155' }}>
      <div style={{ fontSize: '40px' }}>{icon}</div>
      <p style={{ margin: 0, fontSize: '16px', fontWeight: '600' }}>{label}</p>
      <p style={{ margin: 0, fontSize: '13px', color: '#1e293b' }}>Coming soon</p>
    </div>
  );

  return (
    <div style={{
      display: 'flex', flexDirection: 'column', height: '100vh',
      maxWidth: '480px', margin: '0 auto',
      background: '#080d18',
      fontFamily: "'Inter', sans-serif",
      position: 'relative', overflow: 'hidden'
    }}>

      {/* Animated background blobs */}
      <div style={{
        position: 'absolute', width: '300px', height: '300px',
        borderRadius: '50%', top: '-100px', left: '-100px',
        background: 'radial-gradient(circle, rgba(249,115,22,0.08) 0%, transparent 70%)',
        pointerEvents: 'none', zIndex: 0
      }} />
      <div style={{
        position: 'absolute', width: '250px', height: '250px',
        borderRadius: '50%', bottom: '100px', right: '-80px',
        background: 'radial-gradient(circle, rgba(99,102,241,0.08) 0%, transparent 70%)',
        pointerEvents: 'none', zIndex: 0
      }} />

      {/* Status Bar */}
      <div style={{
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        padding: '14px 20px 10px', zIndex: 1, position: 'relative'
      }}>
        <span style={{ fontSize: '15px', fontWeight: '700', color: '#f1f5f9' }}>
          {new Date().getHours()}:{String(new Date().getMinutes()).padStart(2,'0')}
        </span>
        <div style={{
          display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '2px',
          background: 'rgba(249,115,22,0.08)',
          border: '1px solid rgba(249,115,22,0.2)',
          padding: '6px 16px', borderRadius: '20px'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            <Shield size={11} color="#f97316" />
            <span style={{ fontSize: '12px', fontWeight: '800', color: '#f97316', letterSpacing: '0.08em' }}>
              BHAROSA AI
            </span>
          </div>
          <span style={{ fontSize: '9px', fontWeight: '500', color: '#fb923c', letterSpacing: '0.04em', fontStyle: 'italic' }}>
            bharosa aapka, wada hamara
          </span>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
          <Zap size={13} color="#fbbf24" />
          <span style={{ fontSize: '13px', fontWeight: '700', color: '#f1f5f9' }}>84%</span>
        </div>
      </div>

      {/* Content */}
      <div style={{ flex: 1, overflow: 'hidden', display: 'flex', flexDirection: 'column', position: 'relative', zIndex: 1 }}>
        {activeTab === 'home' && <HomeScreen />}
        {activeTab === 'chat' && <ChatScreen />}
        {activeTab === 'library' && <Placeholder label="Library" icon="📚" />}
        {activeTab === 'memory' && <Placeholder label="Memory" icon="🧠" />}
        {activeTab === 'settings' && <Placeholder label="Settings" icon="⚙️" />}
      </div>

      {/* FAB */}
      {activeTab === 'home' && (
        <button onClick={() => setActiveTab('chat')} style={{
          position: 'absolute', bottom: '80px', right: '20px',
          width: '54px', height: '54px', borderRadius: '50%',
          background: 'linear-gradient(135deg, #ea580c, #f97316)',
          border: 'none', cursor: 'pointer',
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          boxShadow: '0 4px 24px rgba(249,115,22,0.45)',
          zIndex: 10, animation: 'pulse 2s infinite'
        }}>
          <Plus size={24} color="white" />
        </button>
      )}

      {/* Bottom Nav */}
      <div style={{
        display: 'flex', borderTop: '1px solid rgba(255,255,255,0.05)',
        background: 'rgba(8,13,24,0.95)', backdropFilter: 'blur(20px)',
        paddingBottom: '8px', position: 'relative', zIndex: 1
      }}>
        {[
          { id: 'home', icon: <Home size={20} />, label: 'Home' },
          { id: 'chat', icon: <MessageCircle size={20} />, label: 'Chat' },
          { id: 'library', icon: <BookOpen size={20} />, label: 'Library' },
          { id: 'memory', icon: <Brain size={20} />, label: 'Memory' },
          { id: 'settings', icon: <Settings size={20} />, label: 'Settings' },
        ].map(tab => (
          <button key={tab.id} onClick={() => setActiveTab(tab.id)} style={{
            flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center',
            gap: '3px', background: 'transparent', border: 'none', cursor: 'pointer',
            padding: '10px 0 4px',
            color: activeTab === tab.id ? '#f97316' : '#334155'
          }}>
            <div style={{
              padding: '5px 14px', borderRadius: '20px',
              background: activeTab === tab.id ? 'rgba(249,115,22,0.12)' : 'transparent',
              transition: 'all 0.2s'
            }}>
              {tab.icon}
            </div>
            <span style={{ fontSize: '10px', fontWeight: activeTab === tab.id ? '700' : '400' }}>
              {tab.label}
            </span>
          </button>
        ))}
      </div>

      <style>{`
        @keyframes bounce { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-5px)} }
        @keyframes growBar { from{width:0} to{width:92%} }
        @keyframes pulse { 0%,100%{box-shadow:0 4px 24px rgba(249,115,22,0.45)} 50%{box-shadow:0 4px 32px rgba(249,115,22,0.7)} }
        ::-webkit-scrollbar { width: 3px; }
        ::-webkit-scrollbar-thumb { background: rgba(249,115,22,0.2); border-radius: 2px; }
        input::placeholder { color: #334155; }
        * { box-sizing: border-box; }
      `}</style>
    </div>
  );
};

export default BharosaApp;