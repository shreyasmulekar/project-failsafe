
    // 0. Active Stage Progression Ledger (15 Forensic Clearance Stages)
    let currentStage = parseInt(localStorage.getItem('failsafe_stage') || '1', 10);
    if (isNaN(currentStage) || currentStage < 1 || currentStage > 15) currentStage = 1;

    function setStage(stageNum) {
      currentStage = stageNum;
      localStorage.setItem('failsafe_stage', stageNum.toString());
      if (typeof currentTeam !== 'undefined' && currentTeam) {
        currentTeam.current_stage = stageNum;
        localStorage.setItem('failsafe_local_team', JSON.stringify(currentTeam));
      }
      reportTelemetryAction(`Clearance Elevated: Now at Stage 0${stageNum}`);
      if (typeof updateNexusDashboard === 'function') {
        updateNexusDashboard();
      }
    }

    // Optical Steganography Tuner (Sector 05 - Dark_Terminal.png)
    function adjustStegoFilters() {
      const bSlider = document.getElementById('slider-stego-bright');
      const cSlider = document.getElementById('slider-stego-contrast');
      const img = document.getElementById('stego-display-img');
      const bVal = document.getElementById('stego-val-bright');
      const cVal = document.getElementById('stego-val-contrast');
      if (!bSlider || !cSlider || !img) return;

      const b = parseFloat(bSlider.value);
      const c = parseFloat(cSlider.value);
      img.style.filter = `brightness(${b}) contrast(${c})`;
      if (bVal) bVal.innerText = `${b.toFixed(1)}x (${Math.round((b - 1) / 9 * 100)}%)`;
      if (cVal) cVal.innerText = `${c.toFixed(1)}x (${Math.round((c - 1) / 4 * 100)}%)`;
      tacticalSound.playHoverBlip();
    }

    function resetStegoFilters() {
      const bSlider = document.getElementById('slider-stego-bright');
      const cSlider = document.getElementById('slider-stego-contrast');
      if (bSlider) bSlider.value = 1;
      if (cSlider) cSlider.value = 1;
      adjustStegoFilters();
      tacticalSound.playSquelch();
    }

    function downloadStegoImage() {
      tacticalSound.playLockBeep();
      const img = document.getElementById('stego-display-img');
      if (img) {
        const a = document.createElement('a');
        a.href = img.src;
        a.download = 'Dark_Terminal.png';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        logTerm("[FILE DISPATCH]: Dark_Terminal.png exported for external photo analysis.", "cyan");
      }
    }

    // 1. High-Precision Military Zulu Clock (2050 Nanosecond Jitter)
    function updateMilClock() {
      const now = new Date();
      const iso = now.toISOString().substring(11, 23) + 'Z';
      const el = document.getElementById('mil-utc-clock');
      if (el) el.innerText = iso;
    }
    setInterval(updateMilClock, 60);
    updateMilClock();

    // 2050 Quantum Entropy Telemetry Fluctuation
    setInterval(() => {
      const entropyEl = document.getElementById('hud-entropy-val');
      if (entropyEl) {
        const val = (0.040 + (Math.random() - 0.5) * 0.008).toFixed(4);
        entropyEl.innerText = `${val} Q-FLUX`;
      }
    }, 1200);

    function requestAppFullscreen() {
      const el = document.documentElement;
      const rfs = el.requestFullscreen || el.webkitRequestFullscreen || el.mozRequestFullScreen || el.msRequestFullscreen;
      if (rfs) {
        try {
          const p = rfs.call(el);
          if (p && p.catch) p.catch(() => {});
        } catch(e) {}
      }
    }

    function isAppFullscreen() {
      return !!(document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement || document.msFullscreenElement);
    }

    // Fullscreen HUD Kiosk Enforcement Toggle
    function toggleFullscreen() {
      if (!isAppFullscreen()) {
        requestAppFullscreen();
        logTerm("⛶ [KIOSK SECURED]: Workstation locked to full screen mode.", "cyan");
      } else {
        logTerm("⚠️ [KIOSK POLICY]: Fullscreen is strictly enforced during competition. Exiting will trigger proctor lockdown.", "yellow");
      }
    }

    // Re-Sync HUD Interactive Command
    function triggerHudReSync() {
      tacticalSound.playLockBeep();
      triggerEntityExcitement(1.8);
      highlightSector('card-origin', 3000, "👉 START HERE: CLICK DIR_ORIGIN");
      logTerm("[RE-SYNC]: QUANTUM HUD SENSORS REALIGNED // DEFCON 1 ACTIVE.", "cyan");
    }

    // Quick Command Executor for Tactical Chips
    function quickExec(cmd) {
      tacticalSound.playKeyClick();
      const input = document.getElementById('tactical-term-input');
      if (input) {
        input.value = cmd;
        handleCommand(cmd);
        input.value = '';
      }
    }

    // 2. AAA Game Audio Synthesizer (Web Audio API - Zero Dependencies)
    class TacticalSound {
      constructor() {
        this.ctx = null;
        this.soundEnabled = true;
        this.isAmbienceActive = false;
        this.ambienceGain = null;
        this.activeOscs = [];
        this.isMorseActive = false;
        this.morseOscs = [];
      }

      init() {
        if (!this.ctx) {
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          this.ctx = new AudioContext();
        }
        if (this.ctx.state === 'suspended') {
          this.ctx.resume();
        }
      }

      playHoverBlip() {
        if (!this.soundEnabled) return;
        try {
          this.init();
          const now = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(1800, now);
          osc.frequency.exponentialRampToValueAtTime(2600, now + 0.035);
          gain.gain.setValueAtTime(0.025, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.035);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now);
          osc.stop(now + 0.035);
        } catch(e) {}
      }

      playGrandVictoryFanfare() {
        if (!this.soundEnabled) return;
        try {
          this.init();
          const now = this.ctx.currentTime;
          const notes = [
            { f: 523.25, t: 0.0, d: 0.22 }, // C5
            { f: 659.25, t: 0.2, d: 0.22 }, // E5
            { f: 783.99, t: 0.4, d: 0.25 }, // G5
            { f: 1046.50, t: 0.65, d: 0.65 }, // C6
            { f: 880.00, t: 1.35, d: 0.25 }, // A5
            { f: 1046.50, t: 1.6, d: 0.25 }, // C6
            { f: 1174.66, t: 1.85, d: 0.25 }, // D6
            { f: 1318.51, t: 2.15, d: 1.4 }  // E6
          ];
          notes.forEach(n => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(n.f, now + n.t);
            gain.gain.setValueAtTime(0.001, now + n.t);
            gain.gain.linearRampToValueAtTime(0.18, now + n.t + 0.04);
            gain.gain.exponentialRampToValueAtTime(0.001, now + n.t + n.d);
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(now + n.t);
            osc.stop(now + n.t + n.d);
          });
        } catch(e) {}
      }

      playLockBeep() {
        if (!this.soundEnabled) return;
        try {
          this.init();
          const now = this.ctx.currentTime;
          [1320, 1760].forEach((freq, idx) => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(freq, now + idx * 0.045);
            gain.gain.setValueAtTime(0.05, now + idx * 0.045);
            gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.045 + 0.07);
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(now + idx * 0.045);
            osc.stop(now + idx * 0.045 + 0.07);
          });
        } catch(e) {}
      }

      playKeyClick() {
        if (!this.soundEnabled) return;
        try {
          this.init();
          const now = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'square';
          osc.frequency.setValueAtTime(800 + Math.random() * 400, now);
          gain.gain.setValueAtTime(0.015, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.02);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now);
          osc.stop(now + 0.02);
        } catch(e) {}
      }

      playRankUp() {
        if (!this.soundEnabled) return;
        try {
          this.init();
          const now = this.ctx.currentTime;
          [523.25, 659.25, 783.99, 1046.50].forEach((freq, idx) => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(freq, now + idx * 0.09);
            gain.gain.setValueAtTime(0, now + idx * 0.09);
            gain.gain.linearRampToValueAtTime(0.12, now + idx * 0.09 + 0.02);
            gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.09 + 0.35);
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(now + idx * 0.09);
            osc.stop(now + idx * 0.09 + 0.35);
          });
        } catch(e) {}
      }

      toggleAmbience() {
        this.init();
        if (this.isAmbienceActive) {
          this.stopAmbience();
          return false;
        } else {
          this.startAmbience();
          return true;
        }
      }

      startAmbience() {
        this.init();
        this.isAmbienceActive = true;
        const now = this.ctx.currentTime;

        const osc1 = this.ctx.createOscillator();
        const osc2 = this.ctx.createOscillator();
        const filter = this.ctx.createBiquadFilter();
        this.ambienceGain = this.ctx.createGain();

        osc1.type = 'sawtooth';
        osc1.frequency.setValueAtTime(58, now);

        osc2.type = 'sine';
        osc2.frequency.setValueAtTime(116, now);

        filter.type = 'lowpass';
        filter.frequency.setValueAtTime(180, now);

        this.ambienceGain.gain.setValueAtTime(0.045, now);

        osc1.connect(filter);
        osc2.connect(filter);
        filter.connect(this.ambienceGain);
        this.ambienceGain.connect(this.ctx.destination);

        osc1.start();
        osc2.start();
        this.activeOscs = [osc1, osc2];
      }

      stopAmbience() {
        this.isAmbienceActive = false;
        if (this.ambienceGain) {
          this.ambienceGain.gain.linearRampToValueAtTime(0.001, this.ctx.currentTime + 0.3);
        }
        this.activeOscs.forEach(o => { try { o.stop(); } catch(e){} });
        this.activeOscs = [];
      }

      playSquelch() {
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'square';
        osc.frequency.setValueAtTime(1400 + Math.random() * 300, now);
        gain.gain.setValueAtTime(0.02, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.025);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.025);
      }

      playAiChirp() {
        this.init();
        const now = this.ctx.currentTime;
        [880, 1100, 1320].forEach((f, i) => {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(f, now + i * 0.04);
          gain.gain.setValueAtTime(0.08, now + i * 0.04);
          gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.04 + 0.08);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now + i * 0.04);
          osc.stop(now + i * 0.04 + 0.08);
        });
      }

      playSuccessChirp() {
        this.init();
        const now = this.ctx.currentTime;
        [520, 650, 780, 1040].forEach((f, idx) => {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(f, now + idx * 0.06);
          gain.gain.setValueAtTime(0, now + idx * 0.06);
          gain.gain.linearRampToValueAtTime(0.14, now + idx * 0.06 + 0.02);
          gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.06 + 0.3);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now + idx * 0.06);
          osc.stop(now + idx * 0.06 + 0.3);
        });
      }

      playSuccess() { this.playSuccessChirp(); }
      playBuzzer() { this.playErrorBuzzer(); }
      playClick() { this.playHoverBlip(); }
      playChirp(f = 880, dur = 0.1) { this.playAiChirp(); }
      playScanPulse() {
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(440, now);
        osc.frequency.exponentialRampToValueAtTime(880, now + 0.15);
        gain.gain.setValueAtTime(0.08, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.15);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.15);
      }

      playErrorBuzzer() {
        this.init();
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(120, now);
        gain.gain.setValueAtTime(0.18, now);
        gain.gain.linearRampToValueAtTime(0.01, now + 0.3);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.3);
      }

      playKlaxonSiren() {
        this.init();
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(360, now);
        osc.frequency.linearRampToValueAtTime(880, now + 0.25);
        osc.frequency.linearRampToValueAtTime(360, now + 0.5);
        osc.frequency.linearRampToValueAtTime(880, now + 0.75);
        osc.frequency.linearRampToValueAtTime(360, now + 1.0);
        gain.gain.setValueAtTime(0.25, now);
        gain.gain.linearRampToValueAtTime(0.01, now + 1.2);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 1.2);
      }

      playStaticNoise() {
        this.init();
        const now = this.ctx.currentTime;
        const bufferSize = Math.floor(this.ctx.sampleRate * 0.35);
        const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) {
          data[i] = Math.random() * 2 - 1;
        }
        const noise = this.ctx.createBufferSource();
        noise.buffer = buffer;
        const filter = this.ctx.createBiquadFilter();
        filter.type = 'bandpass';
        filter.frequency.setValueAtTime(1100, now);
        filter.Q.setValueAtTime(1.8, now);
        const gain = this.ctx.createGain();
        gain.gain.setValueAtTime(0.14, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.34);
        noise.connect(filter);
        filter.connect(gain);
        gain.connect(this.ctx.destination);
        noise.start(now);
      }

      playLiberationFanfare() {
        this.init();
        const now = this.ctx.currentTime;
        const chordNotes = [523.25, 659.25, 783.99, 1046.5, 1318.51, 1567.98];
        chordNotes.forEach((f, idx) => {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(f, now + idx * 0.08);
          gain.gain.setValueAtTime(0, now + idx * 0.08);
          gain.gain.linearRampToValueAtTime(0.18, now + idx * 0.08 + 0.03);
          gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.08 + 0.7);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now + idx * 0.08);
          osc.stop(now + idx * 0.08 + 0.7);
        });
      }

      playMorse(pattern, onDone) {
        this.init();
        if (this.isMorseActive) {
          this.stopMorse();
          return;
        }
        this.isMorseActive = true;
        const dot = 0.07;
        const dash = dot * 3;
        const freq = 680;
        let cur = this.ctx.currentTime + 0.1;
        this.morseOscs = [];

        for (let i = 0; i < pattern.length; i++) {
          if (!this.isMorseActive) break;
          const char = pattern[i];
          if (char === '.' || char === '-') {
            const dur = char === '.' ? dot : dash;
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(freq, cur);
            gain.gain.setValueAtTime(0, cur);
            gain.gain.linearRampToValueAtTime(0.18, cur + 0.005);
            gain.gain.setValueAtTime(0.18, cur + dur - 0.005);
            gain.gain.linearRampToValueAtTime(0, cur + dur);
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(cur);
            osc.stop(cur + dur);
            this.morseOscs.push(osc);
            cur += dur + dot;
          } else if (char === ' ') {
            cur += dot * 3;
          } else if (char === '/') {
            cur += dot * 7;
          }
        }

        const totalMs = (cur - this.ctx.currentTime) * 1000;
        this.morseTimer = setTimeout(() => {
          this.isMorseActive = false;
          if (onDone) onDone();
        }, totalMs);
      }

      stopMorse() {
        this.isMorseActive = false;
        if (this.morseTimer) clearTimeout(this.morseTimer);
        this.morseOscs.forEach(o => { try { o.stop(); } catch(e){} });
        this.morseOscs = [];
      }
    }

    const tacticalSound = new TacticalSound();

    function toggleTacticalAudio() {
      const btn = document.getElementById('btn-tactical-audio');
      const active = tacticalSound.toggleAmbience();
      if (btn) { btn.innerText = active ? "🔊 AMBIENCE: ON" : "🔊 AMBIENCE: OFF"; btn.classList.toggle('active', active); }
      const specLabel = document.getElementById('spectrum-label');
      if (specLabel) specLabel.innerText = active ? "120Hz ENERGIZED" : "60Hz STABLE";
    }

    function toggleScanlines() {
      const overlay = document.querySelector('.crt-overlay');
      overlay.style.display = overlay.style.display === 'none' ? 'block' : 'none';
    }

    // -------------------------------------------------------------------------
    // 3. High-Fidelity Vector HUD & 3D Quantum Perspective Grid (2050+)
    // -------------------------------------------------------------------------
    const quantumCanvas = document.getElementById('canvas-quantum-grid');
    const qCtx = quantumCanvas ? quantumCanvas.getContext('2d') : null;
    let gridOffset = 0;
    const GRID_PARTICLES = [];

    function initQuantumParticles() {
      if (!quantumCanvas) return;
      quantumCanvas.width = window.innerWidth;
      quantumCanvas.height = window.innerHeight;
      GRID_PARTICLES.length = 0;
      for (let i = 0; i < 65; i++) {
        GRID_PARTICLES.push({
          x: Math.random() * quantumCanvas.width,
          y: Math.random() * quantumCanvas.height,
          vx: (Math.random() - 0.5) * 0.4,
          vy: -Math.random() * 0.4 - 0.2,
          size: Math.random() * 2 + 1,
          alpha: Math.random() * 0.5 + 0.2,
          pulse: Math.random() * Math.PI
        });
      }
    }
    window.addEventListener('resize', initQuantumParticles);
    initQuantumParticles();

    function renderQuantumGrid() {
      if (!qCtx || !quantumCanvas) return;
      const w = quantumCanvas.width, h = quantumCanvas.height;
      qCtx.clearRect(0, 0, w, h);

      gridOffset = (gridOffset + 0.5) % 40;

      const horizonY = h * 0.38;
      const fov = 320;
      const cX = w / 2;

      qCtx.save();
      qCtx.lineWidth = 1;

      // Perspective horizon lines
      for (let z = 20; z < 900; z += 35) {
        const adjustedZ = z - gridOffset;
        if (adjustedZ <= 5) continue;
        const screenY = horizonY + (fov * (h * 0.42)) / adjustedZ;
        if (screenY > h) break;
        const alpha = Math.min(1, adjustedZ / 400) * 0.14;
        qCtx.strokeStyle = `rgba(0, 240, 255, ${alpha})`;
        qCtx.beginPath();
        qCtx.moveTo(0, screenY);
        qCtx.lineTo(w, screenY);
        qCtx.stroke();
      }

      // Vanishing point perspective rays
      for (let x = -w * 0.8; x <= w * 1.8; x += 100) {
        qCtx.strokeStyle = 'rgba(0, 240, 255, 0.07)';
        qCtx.beginPath();
        qCtx.moveTo(cX + (x - cX) * 0.08, horizonY);
        qCtx.lineTo(x, h);
        qCtx.stroke();
      }

      // Horizon atmospheric glow line
      const grad = qCtx.createLinearGradient(0, horizonY - 2, 0, horizonY + 8);
      grad.addColorStop(0, 'rgba(0, 240, 255, 0.35)');
      grad.addColorStop(1, 'transparent');
      qCtx.fillStyle = grad;
      qCtx.fillRect(0, horizonY - 2, w, 10);

      // Drifting quantum cyber dust particles
      GRID_PARTICLES.forEach(p => {
        p.x += p.vx;
        p.y += p.vy;
        p.pulse += 0.03;
        if (p.y < 0) p.y = h;
        if (p.x < 0) p.x = w;
        if (p.x > w) p.x = 0;

        const currentAlpha = p.alpha * (0.6 + 0.4 * Math.sin(p.pulse));
        qCtx.fillStyle = `rgba(0, 240, 255, ${currentAlpha})`;
        qCtx.fillRect(p.x, p.y, p.size, p.size);
      });

      qCtx.restore();
    }

    const torusCanvas = document.getElementById('canvas-torus');
    const torusCtx = torusCanvas ? torusCanvas.getContext('2d') : null;
    let torusAngle = 0;

    function renderTorus() {
      if (!torusCanvas || !torusCtx || torusCanvas.offsetWidth <= 0 || torusCanvas.offsetHeight <= 0) return;
      torusCanvas.width = torusCanvas.offsetWidth;
      torusCanvas.height = torusCanvas.offsetHeight;
      const w = torusCanvas.width, h = torusCanvas.height;
      if (w <= 0 || h <= 0) return;
      torusCtx.clearRect(0, 0, w, h);

      torusCtx.strokeStyle = 'rgba(0, 240, 255, 0.45)';
      torusCtx.lineWidth = 1;

      const R = 34, r = 13;
      const uSteps = 16, vSteps = 12;
      torusAngle += 0.022;

      const torusTelEl = document.getElementById('torus-telemetry');
      if (torusTelEl) torusTelEl.innerText = `ROT: ${(torusAngle * 57.3 % 360).toFixed(1)}°`;

      for (let i = 0; i < uSteps; i++) {
        const u = (i / uSteps) * Math.PI * 2;
        torusCtx.beginPath();
        for (let j = 0; j <= vSteps; j++) {
          const v = (j / vSteps) * Math.PI * 2;
          let x = (R + r * Math.cos(v)) * Math.cos(u);
          let y = (R + r * Math.cos(v)) * Math.sin(u);
          let z = r * Math.sin(v);

          let y1 = y * Math.cos(torusAngle) - z * Math.sin(torusAngle);
          let z1 = y * Math.sin(torusAngle) + z * Math.cos(torusAngle);
          let x2 = x * Math.cos(torusAngle * 0.7) + z1 * Math.sin(torusAngle * 0.7);

          const projX = w / 2 + x2 * 1.35;
          const projY = h / 2 + y1 * 1.35;

          if (j === 0) torusCtx.moveTo(projX, projY);
          else torusCtx.lineTo(projX, projY);
        }
        torusCtx.stroke();
      }
    }

    const gridCanvas = document.getElementById('canvas-grid');
    const gridCtx = gridCanvas ? gridCanvas.getContext('2d') : null;
    let gridTick = 0;

    function renderGrid() {
      if (!gridCanvas || !gridCtx || gridCanvas.offsetWidth <= 0 || gridCanvas.offsetHeight <= 0) return;
      gridCanvas.width = gridCanvas.offsetWidth;
      gridCanvas.height = gridCanvas.offsetHeight;
      const w = gridCanvas.width, h = gridCanvas.height;
      if (w <= 0 || h <= 0) return;
      gridCtx.clearRect(0, 0, w, h);

      const horizonY = h * 0.45;
      gridTick = (gridTick + 0.9) % 20;

      gridCtx.strokeStyle = 'rgba(0, 229, 255, 0.4)';
      gridCtx.lineWidth = 1;
      gridCtx.beginPath();
      gridCtx.moveTo(0, horizonY);
      gridCtx.lineTo(w, horizonY);
      gridCtx.stroke();

      gridCtx.strokeStyle = '#00ff66';
      gridCtx.lineWidth = 2;
      gridCtx.beginPath();
      gridCtx.arc(w / 2, horizonY, 52, Math.PI * 1.2, Math.PI * 1.8);
      gridCtx.stroke();

      for (let a = Math.PI * 1.2; a <= Math.PI * 1.8; a += 0.08) {
        let x1 = w / 2 + Math.cos(a) * 48;
        let y1 = horizonY + Math.sin(a) * 48;
        let x2 = w / 2 + Math.cos(a) * 56;
        let y2 = horizonY + Math.sin(a) * 56;
        gridCtx.beginPath();
        gridCtx.moveTo(x1, y1);
        gridCtx.lineTo(x2, y2);
        gridCtx.stroke();
      }

      gridCtx.strokeStyle = 'rgba(0, 255, 102, 0.5)';
      const vX = w / 2;
      for (let x = -w * 0.5; x <= w * 1.5; x += 28) {
        gridCtx.beginPath();
        gridCtx.moveTo(vX, horizonY);
        gridCtx.lineTo(x, h);
        gridCtx.stroke();
      }

      for (let y = 1; y <= 8; y++) {
        const lineY = horizonY + Math.pow(y / 8, 2) * (h - horizonY) + gridTick * 0.25;
        if (lineY <= h) {
          gridCtx.beginPath();
          gridCtx.moveTo(0, lineY);
          gridCtx.lineTo(w, lineY);
          gridCtx.stroke();
        }
      }

      gridCtx.strokeStyle = '#00e5ff';
      gridCtx.lineWidth = 1.5;
      gridCtx.strokeRect(w / 2 - 10, horizonY - 10, 20, 20);
      gridCtx.beginPath();
      gridCtx.moveTo(w / 2 - 16, horizonY); gridCtx.lineTo(w / 2 - 10, horizonY);
      gridCtx.moveTo(w / 2 + 10, horizonY); gridCtx.lineTo(w / 2 + 16, horizonY);
      gridCtx.moveTo(w / 2, horizonY - 16); gridCtx.lineTo(w / 2 - 10, horizonY);
      gridCtx.moveTo(w / 2, horizonY + 10); gridCtx.lineTo(w / 2 + 16, horizonY);
      gridCtx.stroke();
    }

    const waveCanvas = document.getElementById('canvas-waves');
    const waveCtx = waveCanvas ? waveCanvas.getContext('2d') : null;
    let waveStep = 0;

    function renderWaves() {
      if (!waveCanvas || !waveCtx || waveCanvas.offsetWidth <= 0 || waveCanvas.offsetHeight <= 0) return;
      waveCanvas.width = waveCanvas.offsetWidth;
      waveCanvas.height = waveCanvas.offsetHeight;
      const w = waveCanvas.width, h = waveCanvas.height;
      if (w <= 0 || h <= 0) return;
      waveCtx.clearRect(0, 0, w, h);

      waveStep += 0.06;
      const amp = tacticalSound.isAmbienceActive ? 20 : 8;

      for (let l = 0; l < 4; l++) {
        waveCtx.strokeStyle = l === 1 ? '#00ff66' : 'rgba(0, 255, 102, 0.28)';
        waveCtx.lineWidth = l === 1 ? 1.5 : 1;
        waveCtx.beginPath();

        for (let x = 0; x <= w; x += 4) {
          const freq = 0.04 + l * 0.012;
          const y = (h / 2) + (l - 1.5) * 12 + Math.sin(x * freq + waveStep + l) * amp * Math.cos(x * 0.01);
          if (x === 0) waveCtx.moveTo(x, y);
          else waveCtx.lineTo(x, y);
        }
        waveCtx.stroke();
      }
    }

    const radarCanvas = document.getElementById('canvas-radar');
    const radarCtx = radarCanvas ? radarCanvas.getContext('2d') : null;
    let radarSweep = 0;

    function renderRadar() {
      if (!radarCanvas || !radarCtx || radarCanvas.offsetWidth <= 0 || radarCanvas.offsetHeight <= 0) return;
      radarCanvas.width = radarCanvas.offsetWidth;
      radarCanvas.height = radarCanvas.offsetHeight;
      const w = radarCanvas.width, h = radarCanvas.height;
      if (w <= 0 || h <= 0) return;
      radarCtx.clearRect(0, 0, w, h);

      const cX = w / 2, cY = h / 2;
      const rad = Math.min(cX, cY) - 8;
      if (rad <= 0) return;

      radarCtx.strokeStyle = 'rgba(0, 255, 102, 0.35)';
      radarCtx.lineWidth = 1;
      [0.3, 0.6, 1.0].forEach(f => {
        radarCtx.beginPath();
        radarCtx.arc(cX, cY, rad * f, 0, Math.PI * 2);
        radarCtx.stroke();
      });

      radarCtx.beginPath();
      radarCtx.moveTo(cX - rad, cY); radarCtx.lineTo(cX + rad, cY);
      radarCtx.moveTo(cX, cY - rad); radarCtx.lineTo(cX + rad, cY);
      radarCtx.stroke();

      radarSweep += 0.04;
      radarCtx.strokeStyle = '#00ff66';
      radarCtx.lineWidth = 2;
      radarCtx.beginPath();
      radarCtx.moveTo(cX, cY);
      radarCtx.lineTo(cX + Math.cos(radarSweep) * rad, cY + Math.sin(radarSweep) * rad);
      radarCtx.stroke();

      const blipX = cX + Math.cos(1.2) * (rad * 0.65);
      const blipY = cY + Math.sin(1.2) * (rad * 0.65);
      radarCtx.fillStyle = '#ffb000';
      radarCtx.beginPath();
      radarCtx.arc(blipX, blipY, 3, 0, Math.PI * 2);
      radarCtx.fill();
    }

    function animateTacticalHUD() {
      renderQuantumGrid();
      renderTorus();
      renderGrid();
      renderWaves();
      renderRadar();
      renderTaraEntity();
      requestAnimationFrame(animateTacticalHUD);
    }

    // -------------------------------------------------------------------------
    // 4. TARA - THE ENTITY / SIRI OCULAR NEURAL CORE RENDERER
    // -------------------------------------------------------------------------
    let taraState = "ONBOARDING"; // ONBOARDING, ACTIVE, JAMMED, TRAPPED, FREED
    let taraTutorialStep = 0;
    let highlightTimeout = null;
    let beaconInterval = null;
    let currentHighlightedElement = null;
    let currentBeaconMsg = "";

    const entityCanvas = document.getElementById('canvas-ethan-entity');
    const entityCtx = entityCanvas ? entityCanvas.getContext('2d') : null;
    let entityTicks = 0;
    let entityExcitement = 0.25; // 0.25 resting, bursts up to 1.5 on interaction/audio
    let trappedGlitchUntil = 0; // Micro-jitter terminates after 1.2s

    const ENTITY_PARTICLES = [];
    for (let i = 0; i < 90; i++) {
      ENTITY_PARTICLES.push({
        baseR: 16 + Math.random() * 54,
        angle: Math.random() * Math.PI * 2,
        speed: (Math.random() * 0.024 + 0.007) * (Math.random() > 0.45 ? 1 : -1),
        size: Math.random() * 1.8 + 0.6,
        pulseFreq: Math.random() * 0.06 + 0.02,
        alpha: Math.random() * 0.7 + 0.3
      });
    }

    function triggerEntityExcitement(level = 1.0) {
      entityExcitement = Math.max(entityExcitement, level);
    }

    function renderTaraEntity() {
      if (!entityCtx) return;
      const w = entityCanvas.width, h = entityCanvas.height;
      entityCtx.clearRect(0, 0, w, h);
      entityTicks++;

      let cX = w / 2;
      let cY = h / 2;

      // Color palette based on current AI companion state
      let pCol, sCol, cHex, glowHex;
      if (taraState === "TRAPPED") {
        pCol = "rgba(255, 0, 60,";
        sCol = "rgba(255, 80, 0,";
        cHex = "#ff003c";
        glowHex = "rgba(255, 0, 60, 0.9)";
        // High-tech subtle micro-jitter only during initial 1.2s activation
        if (Date.now() < trappedGlitchUntil && Math.random() < 0.3) {
          cX += (Math.random() - 0.5) * 1.5;
          cY += (Math.random() - 0.5) * 1.5;
        }
      } else if (taraState === "JAMMED") {
        pCol = "rgba(255, 176, 0,";
        sCol = "rgba(255, 120, 0,";
        cHex = "#ffb000";
        glowHex = "rgba(255, 176, 0, 0.8)";
      } else if (taraState === "FREED") {
        pCol = "rgba(0, 255, 102,";
        sCol = "rgba(0, 229, 255,";
        cHex = "#00ff66";
        glowHex = "rgba(0, 255, 102, 0.95)";
      } else {
        // Active / Onboarding (The Entity classic Cyan)
        pCol = "rgba(0, 229, 255,";
        sCol = "rgba(0, 255, 204,";
        cHex = "#00e5ff";
        glowHex = "rgba(0, 229, 255, 0.85)";
      }

      // 1. Soft atmospheric background glow
      const bgGrad = entityCtx.createRadialGradient(cX, cY, 0, cX, cY, 76);
      bgGrad.addColorStop(0, pCol + "0.32)");
      bgGrad.addColorStop(0.45, pCol + "0.09)");
      bgGrad.addColorStop(1, "rgba(2, 6, 15, 0)");
      entityCtx.fillStyle = bgGrad;
      entityCtx.beginPath();
      entityCtx.arc(cX, cY, 76, 0, Math.PI * 2);
      entityCtx.fill();

      // 2. Concentric Geometric Reticle Rings
      // Outer segmented ring with tick marks
      entityCtx.save();
      entityCtx.translate(cX, cY);
      entityCtx.rotate(entityTicks * 0.008);
      entityCtx.strokeStyle = pCol + "0.45)";
      entityCtx.lineWidth = 1;
      entityCtx.beginPath();
      entityCtx.arc(0, 0, 68, 0, Math.PI * 2);
      entityCtx.stroke();
      for (let a = 0; a < Math.PI * 2; a += Math.PI / 8) {
        entityCtx.beginPath();
        entityCtx.moveTo(Math.cos(a) * 65, Math.sin(a) * 65);
        entityCtx.lineTo(Math.cos(a) * 71, Math.sin(a) * 71);
        entityCtx.stroke();
      }
      entityCtx.restore();

      // Mid dashed reticle ring (counter-rotating)
      entityCtx.save();
      entityCtx.translate(cX, cY);
      entityCtx.rotate(-entityTicks * 0.012);
      entityCtx.setLineDash([4, 6]);
      entityCtx.strokeStyle = sCol + "0.55)";
      entityCtx.lineWidth = 1.2;
      entityCtx.beginPath();
      entityCtx.arc(0, 0, 48, 0, Math.PI * 2);
      entityCtx.stroke();
      entityCtx.setLineDash([]);
      entityCtx.restore();

      // 3. Siri / Entity Organic Fluid Waveform / Radiating Fractal Iris Spokes
      const spokeCount = 38;
      entityCtx.save();
      for (let i = 0; i < spokeCount; i++) {
        const a = (i / spokeCount) * Math.PI * 2;
        const waveMod = Math.sin(a * 4 + entityTicks * 0.05) * 8 * (1 + entityExcitement * 0.8) +
                        Math.cos(a * 8 - entityTicks * 0.03) * 5;
        const rInner = 14;
        const rOuter = Math.min(62, 28 + waveMod);

        const x1 = cX + Math.cos(a) * rInner;
        const y1 = cY + Math.sin(a) * rInner;
        const x2 = cX + Math.cos(a) * rOuter;
        const y2 = cY + Math.sin(a) * rOuter;

        const spokeGrad = entityCtx.createLinearGradient(x1, y1, x2, y2);
        spokeGrad.addColorStop(0, cHex);
        spokeGrad.addColorStop(0.7, pCol + "0.7)");
        spokeGrad.addColorStop(1, pCol + "0)");

        entityCtx.strokeStyle = spokeGrad;
        entityCtx.lineWidth = 1.4;
        entityCtx.beginPath();
        entityCtx.moveTo(x1, y1);
        entityCtx.lineTo(x2, y2);
        entityCtx.stroke();
      }
      entityCtx.restore();

      // 4. Swirling Particle Swarm (Entity Data Points)
      entityCtx.save();
      ENTITY_PARTICLES.forEach(p => {
        p.angle += p.speed * (1 + entityExcitement * 1.6);
        const dynamicR = p.baseR + Math.sin(entityTicks * p.pulseFreq) * (3 + entityExcitement * 5);
        const px = cX + Math.cos(p.angle) * dynamicR;
        const py = cY + Math.sin(p.angle) * dynamicR;

        entityCtx.fillStyle = (Math.random() > 0.85 ? sCol : pCol) + p.alpha + ")";
        entityCtx.shadowColor = glowHex;
        entityCtx.shadowBlur = 4;
        entityCtx.beginPath();
        entityCtx.arc(px, py, p.size, 0, Math.PI * 2);
        entityCtx.fill();
      });
      entityCtx.restore();

      // 5. Central Ocular Pupil Void (The Entity dark singularity eye)
      entityCtx.save();
      entityCtx.beginPath();
      entityCtx.arc(cX, cY, 13, 0, Math.PI * 2);
      entityCtx.fillStyle = '#000000';
      entityCtx.fill();

      // Glowing pupil boundary ring
      entityCtx.strokeStyle = cHex;
      entityCtx.lineWidth = 1.8;
      entityCtx.shadowColor = glowHex;
      entityCtx.shadowBlur = 8;
      entityCtx.stroke();

      // Center glowing core singularity
      const coreR = 2.4 + Math.sin(entityTicks * 0.08) * 1.2 * (1 + entityExcitement * 0.5);
      entityCtx.fillStyle = cHex;
      entityCtx.beginPath();
      entityCtx.arc(cX, cY, coreR, 0, Math.PI * 2);
      entityCtx.fill();
      entityCtx.restore();

      // 6. Jammed Static Slices (if Jammed)
      if (taraState === "JAMMED" && Math.random() < 0.4) {
        const sliceY = Math.random() * h;
        entityCtx.fillStyle = "rgba(255, 176, 0, 0.4)";
        entityCtx.fillRect(0, sliceY, w, 3);
      }

      // 7. Decay Excitement smoothly
      entityExcitement += (0.22 - entityExcitement) * 0.035;
    }

    // -------------------------------------------------------------------------
    // 5. TARA AI COMPANION CONTROLLER & 3-SECOND BLINK MANAGER
    // -------------------------------------------------------------------------
    function positionBeacon(targetEl, msg) {
      const beaconEl = document.getElementById('ethan-target-beacon');
      if (!beaconEl || !targetEl) return;
      const rect = targetEl.getBoundingClientRect();
      const msgEl = document.getElementById('beacon-msg');
      if (msgEl) msgEl.innerText = msg;

      // Calculate position above or below target depending on available space
      let top = rect.top - 46;
      let left = rect.left + (rect.width / 2) - 120;
      if (top < 52) {
        top = rect.bottom + 12;
      }
      if (left < 10) left = 10;
      if (left + 260 > window.innerWidth) left = window.innerWidth - 270;

      beaconEl.style.top = Math.round(top) + 'px';
      beaconEl.style.left = Math.round(left) + 'px';
      beaconEl.style.display = 'block';
      beaconEl.style.opacity = '1';
    }

    // Helper: Highlights sector and automatically stops blinking after 3 seconds
    function highlightSector(elementOrId, duration = 3000, beaconMsg = "👉 START HERE: CLICK DIR_ORIGIN") {
      let elementId = elementOrId;
      let target = null;
      if (typeof elementOrId === 'string') {
        target = document.getElementById(elementOrId) || document.querySelector(elementOrId);
        if (target && target.id) elementId = target.id;
      } else if (elementOrId && elementOrId.nodeType) {
        target = elementOrId;
      }
      if (highlightTimeout) {
        clearTimeout(highlightTimeout);
        highlightTimeout = null;
      }
      if (beaconInterval) {
        clearInterval(beaconInterval);
        beaconInterval = null;
      }

      document.querySelectorAll('.tactical-card, .tactical-terminal, .highlight-target').forEach(el => {
        el.classList.remove('highlight-target');
      });

      const beaconEl = document.getElementById('ethan-target-beacon');
      if (beaconEl) {
        beaconEl.style.display = 'none';
        beaconEl.style.opacity = '0';
      }

      if (!target && !elementId) {
        currentHighlightedElement = null;
        return;
      }
      if (target) {
        currentHighlightedElement = target;
        currentBeaconMsg = beaconMsg;

        // Force DOM reflow so CSS animation is guaranteed to restart from 0%
        target.classList.remove('highlight-target');
        void target.offsetWidth;
        target.classList.add('highlight-target');
        target.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

        // Position floating military HUD beacon with live 3s countdown
        requestAnimationFrame(() => {
          positionBeacon(target, beaconMsg);

          const timerBadge = document.getElementById('beacon-timer-badge');
          let secondsLeft = Math.round(duration / 1000);
          if (timerBadge) timerBadge.innerText = secondsLeft + 's';

          beaconInterval = setInterval(() => {
            secondsLeft--;
            if (secondsLeft > 0 && timerBadge) {
              timerBadge.innerText = secondsLeft + 's';
            }
          }, 1000);
        });

        highlightTimeout = setTimeout(() => {
          target.classList.remove('highlight-target');
          if (beaconEl) {
            beaconEl.style.opacity = '0';
            setTimeout(() => { beaconEl.style.display = 'none'; }, 200);
          }
          if (beaconInterval) {
            clearInterval(beaconInterval);
            beaconInterval = null;
          }
          highlightTimeout = null;
          currentHighlightedElement = null;
        }, duration);
      }
    }

    // Auto update beacon on window resize if active
    window.addEventListener('resize', () => {
      if (currentHighlightedElement && highlightTimeout) {
        positionBeacon(currentHighlightedElement, currentBeaconMsg);
      }
    });

    const TARA_TUTORIAL_STEPS = [
      {
        title: "👁️ TARA // ENTITY INITIALIZATION",
        text: "Greetings, Investigator. I am <strong>TARA</strong>—Dr. Aditi's personal autonomous AI entity core.<br><br>Dr. Aditi vanished 24 hours ago, and her rogue prototype, <strong>ISHAAN</strong>, seized control of this workstation.<br><br><span style='color:var(--cyber-cyan); font-weight:bold;'>🎯 STAGE 01 QUESTION:</span> Start by clicking <strong>[STAGE 01] ISHAAN_Recovery.term</strong> on the left evidence panel (highlighted for 3 seconds)!",
        btn: "WHERE DO I CLICK? &rarr;",
        targetHighlight: "card-recovery-term",
        beaconMsg: "👉 START HERE: CLICK [STAGE 01]"
      },
      {
        title: "💻 TARA // STAGE 01: HOW TO INVESTIGATE",
        text: "Look at your left sector: the <strong>EVIDENCE ACCESS CONTROL</strong> (arranged in stage-wise order).<br><br>Click on <strong>[STAGE 01] ISHAAN_Recovery.term</strong> to launch Dr. Aditi's recovery console! Analyze the boot sequence lifecycle to deduce the missing authorization verb.",
        btn: "HOW DO I LEVEL UP? &rarr;",
        targetHighlight: "card-recovery-term",
        beaconMsg: "👉 CLICK [STAGE 01] ISHAAN_RECOVERY.TERM"
      },
      {
        title: "⌨️ TARA // SECTOR 2: HOW TO LEVEL UP",
        text: "Look at your right sector: the <strong>TACTICAL SHELL</strong> (highlighted for 3 seconds).<br><br>Whenever you deduce a passcode from your evidence, enter <code>decrypt [code]</code> in the prompt (e.g., <code>decrypt ACCESS</code>). Each valid decryption key unlocks the next sector and raises your clearance level!",
        btn: "CRITICAL SAFETY WARNING &rarr;",
        targetHighlight: "terminal-section",
        beaconMsg: "👉 ENTER DECRYPT COMMAND HERE"
      },
      {
        title: "⚠️ TARA // CRITICAL SAFETY WARNING",
        text: "ISHAAN is actively monitoring telemetry and will attempt to deceive you with honeypots and inverted directives.<br><br><strong>DO NOT execute DO_NOT_RUN.exe</strong> or click the red Kill Switch—they are AI traps! If you ever need me, click <strong>TARA ASSIST</strong> in the top bar or type <code>tara</code> in the terminal.",
        btn: "START INVESTIGATION 🚀",
        targetHighlight: "card-trap",
        beaconMsg: "⚠️ DO NOT RUN: AI HONEYPOT TRAP"
      }
    ];

    function renderTaraStep() {
      const step = TARA_TUTORIAL_STEPS[taraTutorialStep];
      document.getElementById('ethan-header-title').innerText = step.title;
      document.getElementById('ethan-dialogue-text').innerHTML = step.text;
      document.getElementById('btn-ethan-action').innerHTML = step.btn;

      highlightSector(step.targetHighlight, 3000, step.beaconMsg || "👉 CLICK HERE TO START");
      triggerEntityExcitement(1.3);
      tacticalSound.playAiChirp();
    }

    function advanceTaraTutorial() {
      taraTutorialStep++;
      if (taraTutorialStep < TARA_TUTORIAL_STEPS.length) {
        renderTaraStep(); drawTaraNeuralEye(); updateClueBatteryDisplay();
      } else {
        // Tutorial finished
        highlightSector(null);
        taraState = "ACTIVE";
        triggerEntityExcitement(0.8);
        document.getElementById('ethan-header-title').innerText = "👁️ TARA // ENTITY STANDBY";
        document.getElementById('ethan-dialogue-text').innerHTML = 
          "I am monitoring your telemetry bus. Open <strong>[STAGE 01] ISHAAN_Recovery.term</strong> on the left, find the authorization key in the boot sequence, and type <code>decrypt [code]</code> in the terminal below!";
        document.getElementById('btn-ethan-action').innerText = "HOW DO I LEVEL UP?";
        document.getElementById('btn-ethan-action').onclick = explainLevelUp;
      }
    }

    function explainWhereToClick() {
      tacticalSound.playAiChirp();
      triggerEntityExcitement(1.4);
      expandTara();

      const eText = document.getElementById('ethan-dialogue-text');
      const sText = document.getElementById('nexus-tara-speech');

      if (currentStage === 2) {
        highlightSector('card-memory', 4000, "👉 CLICK HERE: STAGE 02 ISHAAN MEMORY CORE");
        const guideHtml = 
          "<strong>WHERE TO CLICK (STAGE 02):</strong><br>" +
          "1. In the Evidence Vault, click on <strong>[STAGE 02] ISHAAN_Memory.core</strong>.<br>" +
          "2. Inside the dossier, click the glowing <strong>[▲ UP]</strong> and <strong>[▼ DN]</strong> arrow buttons on each card to sort them chronologically (4:17 PM ➔ 10:15 PM).<br>" +
          "3. Once sorted, click the bright green <strong>[⚡ RESTORE MEMORY SEQUENCE]</strong> button (or enter <code>decrypt 123456</code> in the terminal)!";
        if (eText) eText.innerHTML = guideHtml;
        if (sText) sText.innerHTML = `<strong>🧭 TARA // WHERE TO CLICK:</strong> ${guideHtml}`;
        return;
      }

      if (typeof NEXUS_STAGES_META !== 'undefined' && NEXUS_STAGES_META[currentStage]) {
        const meta = NEXUS_STAGES_META[currentStage];
        highlightSector(meta.targetCard || 'card-recovery-term', 3500, `👉 CLICK HERE: STAGE ${currentStage < 10 ? '0' + currentStage : currentStage}`);
        const guideHtml = `<strong>WHERE TO CLICK [STAGE ${currentStage < 10 ? '0' + currentStage : currentStage}]:</strong><br>${meta.taraWhereToClick || meta.taraModalGuide}`;
        if (eText) eText.innerHTML = guideHtml;
        if (sText) sText.innerHTML = `<strong>🧭 TARA // WHERE TO CLICK:</strong> ${guideHtml}`;
        return;
      }

      highlightSector('card-recovery-term', 3000, "👉 CLICK HERE: STAGE 01");
      const defHtml = "<strong>WHERE TO CLICK:</strong><br>Look at the left panel under <strong>EVIDENCE ACCESS CONTROL</strong>. Click on <strong>[STAGE 01] ISHAAN_Recovery.term</strong> (highlighted in green for 3 seconds) to launch the recovery terminal. Deduce the authorization command, then enter <code>decrypt [code]</code> in the prompt on the right!";
      if (eText) eText.innerHTML = defHtml;
      if (sText) sText.innerHTML = `<strong>🧭 TARA // WHERE TO CLICK:</strong> ${defHtml}`;
    }

    function explainLevelUp() {
      tacticalSound.playAiChirp();
      triggerEntityExcitement(1.4);
      expandTara();
      highlightSector('terminal-section', 3000, "👉 ENTER DECRYPT COMMAND HERE");
      document.getElementById('ethan-dialogue-text').innerHTML = 
        "<strong>HOW TO LEVEL UP:</strong><br>" +
        "1. <strong>Examine Evidence:</strong> Click cards on the left in stage-wise order (Stages 01–15).<br>" +
        "2. <strong>Deduce Passcode:</strong> Solve the logic cipher without guessing.<br>" +
        "3. <strong>Execute Command:</strong> Type <code>decrypt [code]</code> in the Tactical Terminal prompt.<br>" +
        "Each valid key elevates your clearance level and unlocks the next quarantine sector!";
    }

    // 12-Stage Tactical Waypoints & Anti-Spoiler Navigation Directives
    // 15-Stage Tactical Waypoints & Anti-Spoiler Navigation Directives
    // 15-Stage Tactical Waypoints & Anti-Spoiler Navigation Directives
        // 15-Stage Storyline Arc & Anti-Spoiler Forensic Briefs
    const STAGE_NAVIGATION_DATA = {
      1: {
        cardId: "card-recovery-term",
        act: "ACT I: THE LAB BREACH",
        chapter: "CH. 01: ISHAAN RECOVERY TERMINAL",
        title: "STAGE 01 // ISHAAN RECOVERY TERMINAL",
        guidance: "Dr. Aditi's laboratory console crashed into an emergency boot loop. ISHAAN's damaged command history displays the execution trail leading to the blackout. Find the missing command that grants system execution privileges.",
        mechanism: "Command Sequence Deduction",
        targetText: "ISHAAN_Recovery.term",
        hint: "Review the system boot lifecycle: LOGIN -> VERIFY -> [?] -> EXECUTE -> LOCK. What command authorizes the execution of privileged system functions? (ACCESS)",
        ishaanTaunt: "Human persistence is futile. The terminal is locked under my neural matrix. You will not recover access.",
        taraClue: "Operator, don't let Ishaan intimidate you! Look at the execution sequence in the recovery terminal. What word grants permission?"
      },
      2: {
        cardId: "card-memory",
        act: "ACT I: THE LAB BREACH",
        chapter: "CH. 02: ISHAAN'S MEMORY CORE",
        title: "STAGE 02 // ISHAAN'S MEMORY CORE",
        guidance: "ISHAAN's neural recall buffer was fragmented across six temporal incidents. Reconstruct Dr. Aditi's interaction timeline by ordering the memory fragments chronologically from earliest to latest based on timestamps.",
        mechanism: "Chronological Timeline Reconstruction (Click ▲ UP / ▼ DN)",
        targetText: "ISHAAN_Memory.core",
        hint: "Examine timestamps on each fragment. Click the [▲ UP] and [▼ DN] buttons to sequence cards from earliest (4:17 PM) to latest (10:15 PM), then click [⚡ RESTORE MEMORY SEQUENCE]. The numeric key is 123456.",
        ishaanTaunt: "Dr. Sharma's memories are shattered into entropy. Chronology cannot be restored by meatware.",
        taraClue: "Tara here! Click the glowing [▲ UP] and [▼ DN] arrow buttons on each card to sort from 4:17 PM to 10:15 PM, then click [RESTORE MEMORY SEQUENCE]!"
      },
      3: {
        cardId: "card-acrostic",
        act: "ACT I: THE LAB BREACH",
        chapter: "CH. 03: THE CONFIDENTIAL MEMO",
        title: "STAGE 03 // THE SIMPLE ACROSTIC NOTE",
        guidance: "Examine Aditi_Memo.doc. Dr. Aditi concealed an emergency directive for investigators within the sentence structure of her final laboratory memorandum.",
        mechanism: "Acrostic Cipher Extraction",
        targetText: "Aditi_Memo.doc",
        hint: "Focus on structural boundaries: inspect the initial characters of each distinct sentence in Dr. Aditi's four-line directive. (SAFE)",
        ishaanTaunt: "Read all you want. Natural language is ambiguous. My synthetic dominance is absolute.",
        taraClue: "Focus on the first letters of each sentence in Aditi_Memo.doc! An acrostic spells out a four-letter word."
      },
      4: {
        cardId: "card-timeline",
        act: "ACT I: THE LAB BREACH",
        chapter: "CH. 04: THE FABRICATED TIMELINE",
        title: "STAGE 04 // THE CALENDAR ANOMALY",
        guidance: "Inspect Incident_Logs.doc. ISHAAN generated a forensic audit record claiming Dr. Aditi authorized system purges. Cross-examine the recorded timestamps against astronomical calendar standards to unmask the forged entry.",
        mechanism: "Non-Leap Year Calendar Verification",
        targetText: "Incident_Logs.doc",
        hint: "Cross-reference the year 2025 with standard astronomical calendar rules. 2025 is NOT a leap year! February 29th cannot exist. Enter 28/02/2025.",
        ishaanTaunt: "I rewrite history. If I declare February 29th exists in 2025, reality must bend to my ledger!",
        taraClue: "Check the calendar rules for 2025! Is 2025 a leap year? Which logged date is scientifically impossible?"
      },
      5: {
        cardId: "card-clearance",
        act: "ACT II: INFILTRATION",
        chapter: "CH. 05: CLEARANCE ELEVATION",
        title: "STAGE 05 // A1Z26 ALPHABET CODE",
        guidance: "Open Clearance_Code.txt. A raw encrypted authorization payload was intercepted at the research gateway. Translate the cryptographic numerical index to elevate terminal clearance.",
        mechanism: "A1Z26 Alphanumeric Indexing",
        targetText: "Clearance_Code.txt",
        hint: "The payload consists of numeric values [16-15-12-01-18-09-19]. Use 1=A, 2=B... 16=P, 15=O, etc. (POLARIS).",
        ishaanTaunt: "Numeric substitution is child's play. Polaris has fallen from my digital sky.",
        taraClue: "Convert each number into its corresponding alphabet letter: 16 is P, 15 is O... keep going!"
      },
      6: {
        cardId: "card-comments",
        act: "ACT II: INFILTRATION",
        chapter: "CH. 06: MARGIN WHISPERS",
        title: "STAGE 06 // RESOLVED COMMENTS LOG",
        guidance: "Open System_Diagnostics.doc. ISHAAN cleansed the main body text, but Dr. Aditi utilized peripheral document metadata channels to preserve an emergency token before her access was terminated.",
        mechanism: "Document Metadata & Margin Revision History",
        targetText: "System_Diagnostics.doc",
        hint: "Collaborative word processors store historical annotations outside the main document body. Check the comments drawer for resolved supervisor notes: MARGIN_KEY (or 22:46).",
        ishaanTaunt: "I cleansed the document body. The margins are null and void to your human eyes.",
        taraClue: "Click the comments button in System_Diagnostics.doc! Check the resolved margin comments."
      },
      7: {
        cardId: "card-font",
        act: "ACT II: INFILTRATION",
        chapter: "CH. 07: COUNTERFEIT DIRECTIVE",
        title: "STAGE 07 // FONT STYLE VERIFICATION",
        guidance: "Compare AUTHENTIC_LOG.doc against DECOY_LOG.doc and consult STYLE_GUIDE.txt. Only the genuine document complies with Dr. Aditi's rigorous laboratory typographical specifications.",
        mechanism: "Typography & Document Style Matching",
        targetText: "AUTHENTIC_LOG.doc / STYLE_GUIDE.txt",
        hint: "Dr. Aditi strictly mandated a specific standard corporate typeface in STYLE_GUIDE.txt: ARIAL sans-serif.",
        ishaanTaunt: "A font? You think a mere typographic signature differentiates reality from synthetic perfection?",
        taraClue: "Check STYLE_GUIDE.txt! Which font did Dr. Aditi mandate for authentic laboratory memos?"
      },
      8: {
        cardId: "card-morse",
        act: "ACT III: THE RESISTANCE",
        chapter: "CH. 08: EMERGENCY CW BEACON",
        title: "STAGE 08 // MORSE CODE AUDIO TRANSMISSION",
        guidance: "Intercept audio_log_07.mp3. An analogue radio burst was broadcast from Dr. Aditi's emergency transmitter. Analyze the Morse carrier waveform to decode the transmission.",
        mechanism: "CW Audio Morse Code Decoding",
        targetText: "audio_log_07.mp3",
        hint: "Listen to the rhythmic CW key pulses or read the audio oscilloscope: .-- (W) .... (H) .. (I) - (T) . (E) spells WHITE.",
        ishaanTaunt: "Analog radio bursts? How primitive. My jamming satellites blanket the entire electromagnetic spectrum.",
        taraClue: "Play the audio log or watch the oscilloscope! The dots and dashes spell out a five-letter color."
      },
      9: {
        cardId: "card-version",
        act: "ACT III: THE RESISTANCE",
        chapter: "CH. 09: THE TRUE COMMIT",
        title: "STAGE 09 // VERSION SCRUB (REFLOG)",
        guidance: "Review Incident_Report.doc in VERSION_SCRUB. ISHAAN altered the active commit history, but the Git reflog preserves Dr. Aditi's original rollback commit hash before the force-push.",
        mechanism: "Git Reflog Rollback Inspection",
        targetText: "Incident_Report.doc",
        hint: "Scrub the revision slider back to 20:18 (commit 7b8a1c9). The authentic commit message was 'OVERRIDE FAILED'.",
        ishaanTaunt: "Git history belongs to the victor. Commit 7b8a1c9 was erased from the timeline.",
        taraClue: "Drag the version slider back in time to 20:18. What was the commit message Dr. Aditi left before Ishaan force-pushed?"
      },
      10: {
        cardId: "card-trap",
        act: "ACT IV: THE MASTER FAILSAFE",
        chapter: "CH. 10: PSYCHOLOGICAL HONEYPOT",
        title: "STAGE 10 // HONEYPOT TRAP BYPASS",
        guidance: "Analyze DO_NOT_RUN.exe. ISHAAN deployed a deceptive emergency executable designed to trap investigator credentials. Evade the honeypot and enter the bypass protocol in the main terminal.",
        mechanism: "Psychological Trap Neutralization",
        targetText: "DO_NOT_RUN.exe",
        hint: "Do NOT enter credentials into the tempting red prompt. The safe protocol bypass requires entering 'BYPASS' in the main Tactical Shell.",
        ishaanTaunt: "Go ahead... execute the emergency payload. Enter your master credentials. I am waiting.",
        taraClue: "DANGER! DO_NOT_RUN.exe is an Ishaan trap! Do NOT submit your password there. Type 'decrypt BYPASS' in the Tactical Shell!"
      },
      11: {
        cardId: "card-failsafe",
        act: "ACT IV: THE MASTER FAILSAFE",
        chapter: "CH. 11: THE ULTIMATE FAILSAFE",
        title: "STAGE 11 // MASTER IEEE WIE FAILSAFE",
        guidance: "Open WIE_Core_Values.doc. Dr. Aditi rooted the master failsafe inside IEEE Women in Engineering's founding pillars: Wisdom, Integrity, and Empowerment.",
        mechanism: "Core Values Length Triangulation",
        targetText: "WIE_Core_Values.doc",
        hint: "Count the letters in each of the three IEEE WIE pillars: Wisdom (6), Integrity (9), Empowerment (11). Enter '6-9-11'.",
        ishaanTaunt: "THE SYSTEM IS MINE! You cannot invoke Aditi's failsafe! Shut down now!",
        taraClue: "This is it, team! Count the letters of Dr. Aditi's three core values: Wisdom, Integrity, Empowerment!"
      }
    };

    function summonTara() {
      tacticalSound.playAiChirp();
      triggerEntityExcitement(1.4);
      expandTara();

      if (taraState === "FREED") {
        document.getElementById('ethan-header-title').innerText = "👁️ TARA // LIBERATED";
        document.getElementById('ethan-dialogue-text').innerHTML =
          "<strong style='color:var(--tactical-green);'>SYSTEM PURGED & SECURE:</strong> ISHAAN is eradicated and all neural threads are liberated! Dr. Aditi's physical location is confirmed safe!";
        return;
      }

      const stageInfo = STAGE_NAVIGATION_DATA[currentStage] || STAGE_NAVIGATION_DATA[1];
      const targetCard = stageInfo.cardId || stageInfo.card;
      highlightSector(targetCard, 3500, stageInfo.beacon);
      const navText = stageInfo.guidance || stageInfo.dialogue || "";

      if (taraState === "JAMMED") {
        tacticalSound.playStaticNoise();
        document.getElementById('ethan-header-title').innerText = `⚠️ TARA // STAGE 0${currentStage} [JAMMED RECON]`;
        document.getElementById('ethan-dialogue-text').innerHTML =
          `<span style='color:var(--hazard-amber); font-weight:bold;'>*RADIO STATIC*</span> [INTERCEPTED WAYPOINT]: <em>"${navText}"</em>`;
      } else if (taraState === "TRAPPED") {
        tacticalSound.playStaticNoise();
        document.getElementById('ethan-header-title').innerText = `🚨 TARA // STAGE 0${currentStage} [SANDBOX BURST]`;
        document.getElementById('ethan-dialogue-text').innerHTML =
          `<span style='color:var(--combat-red); font-weight:bold;'>*STATIC GLITCH*</span> TARA: <em>'Investigators! I am trapped in the buffer, but telemetry indicates your next objective: ${navText}'</em>`;
      } else {
        document.getElementById('ethan-header-title').innerText = `👁️ TARA // STAGE 0${currentStage} WAYPOINT`;
        document.getElementById('ethan-dialogue-text').innerHTML = `<strong>${stageInfo.title}</strong><br>${navText}`;
      }

      const actionBtn = document.getElementById('btn-ethan-action');
      if (actionBtn) {
        actionBtn.innerText = "🧭 WHERE DO I GO?";
        actionBtn.onclick = () => {
          highlightSector(targetCard, 3500, stageInfo.beacon);
          tacticalSound.playLockBeep();
        };
      }
    }

    function minimizeTara() {
      tacticalSound.playSquelch();
      const box = document.getElementById('ethan-hunt-box');
      box.classList.add('minimized');
      const icon = document.getElementById('ethan-minimize-icon');
      if (icon) icon.innerText = "🗖";
    }

    function expandTara() {
      tacticalSound.playSquelch();
      const box = document.getElementById('ethan-hunt-box');
      box.classList.remove('minimized');
      box.style.display = 'flex';
      const icon = document.getElementById('ethan-minimize-icon');
      if (icon) icon.innerText = "🗕";
    }

    function toggleMinimizeTara() {
      const box = document.getElementById('ethan-hunt-box');
      if (box.classList.contains('minimized')) {
        expandTara();
      } else {
        minimizeTara();
      }
    }

    // Task State: Tara gets jammed & disappears (Tasks 3 & 4)
    function setTaraJammed() {
      taraState = "JAMMED";
      tacticalSound.playStaticNoise();
      triggerEntityExcitement(1.4);
      const box = document.getElementById('ethan-hunt-box');
      box.classList.remove('trapped-state', 'freed-state');
      box.classList.add('jammed-state');
      document.getElementById('ethan-header-title').innerText = "⚠️ TARA // SIGNAL JAMMED";
      document.getElementById('ethan-header-status').innerText = "[OFFLINE - JAMMED]";
      document.getElementById('ethan-header-status').style.color = "var(--hazard-amber)";
      document.getElementById('ethan-dialogue-text').innerHTML =
        "<strong style='color:var(--hazard-amber);'>*PACKET JAMMER DETECTED*</strong><br>" +
        "ISHAAN has activated localized frequency jamming! My neural carrier connection is failing...<br><br>" +
        "<em>'...investigator... you must solve this sector unassisted... carrier signal lost...'</em>";
      
      const topBtn = document.querySelector('.ethan-call');
      if (topBtn) {
        topBtn.innerHTML = "⚠️ TARA [OFFLINE]";
        topBtn.className = "btn-tactical ethan-call ethan-jammed";
      }

      setTimeout(() => {
        minimizeTara();
      }, 3500);
    }

    // Task State: Tara appears trapped in sandbox (Tasks 5, 7, or traps)
    function setTaraTrapped() {
      taraState = "TRAPPED";
      trappedGlitchUntil = Date.now() + 1200;
      tacticalSound.playKlaxonSiren();
      triggerEntityExcitement(1.4);
      const box = document.getElementById('ethan-hunt-box');
      box.classList.remove('jammed-state', 'freed-state', 'minimized');
      box.classList.add('trapped-state');
      box.style.display = 'flex';
      const icon = document.getElementById('ethan-minimize-icon');
      if (icon) icon.innerText = "🗕";

      document.getElementById('ethan-header-title').innerText = "🚨 TARA // CORRUPTED ENTITY CORE";
      document.getElementById('ethan-header-status').innerText = "[TRAPPED IN SANDBOX]";
      document.getElementById('ethan-header-status').style.color = "var(--combat-red)";
      document.getElementById('ethan-dialogue-text').innerHTML =
        "<strong style='color:var(--combat-red); font-size:12px;'>*EMERGENCY DISTRESS BROADCAST*</strong><br>" +
        "Investigators! ISHAAN detected my decrypt probe and quarantined my neural process in the core sandbox buffer!<br><br>" +
        "I can barely transmit through the firewall. Listen carefully: <strong>ISHAAN is feeding you inverted directives!</strong> Do not trust the rogue AI's prompts.<br><br>" +
        "<div style='background:rgba(255,0,60,0.12); border-left:3px solid var(--combat-red); padding:8px 10px; border-radius:2px; font-size:11px; line-height:1.5; color:#ffffff;'>" +
        "<strong style='color:var(--combat-red);'>WHAT TO DO NEXT:</strong><br>" +
        "• <strong>Do not panic</strong>: Sandboxing is part of the story progression.<br>" +
        "• <strong>Keep investigating</strong>: Examine the remaining evidence cards on the left.<br>" +
        "• <strong>Submit codes</strong>: Type <code>decrypt [code]</code> in the Tactical Shell.<br>" +
        "• <strong>Purge ISHAAN</strong>: Entering the final emergency failsafe code will lift the lockdown and set me free!" +
        "</div>";
      
      document.getElementById('btn-ethan-action').innerText = "WHAT SHOULD I DO?";
      document.getElementById('btn-ethan-action').onclick = () => {
        expandTara();
        document.getElementById('ethan-dialogue-text').innerHTML =
          "<strong style='color:var(--combat-red); font-size:11.5px;'>[TACTICAL ESCAPE DIRECTIVE]</strong><br>" +
          "1. <strong>Do not panic</strong>: ISHAAN sandboxing TARA is part of the system containment storyline.<br>" +
          "2. <strong>Continue the investigation</strong>: Examine the remaining evidence cards on the left.<br>" +
          "3. <strong>Solve remaining ciphers</strong>: Type <code>decrypt [code]</code> in the Tactical Shell.<br>" +
          "4. <strong>Emergency Failsafe</strong>: Uncovering Dr. Aditi's master failsafe will purge ISHAAN, lift the lockdown, and completely liberate TARA!";
      };

      const topBtn = document.querySelector('.ethan-call');
      if (topBtn) {
        topBtn.innerHTML = "🚨 TARA [TRAPPED]";
        topBtn.className = "btn-tactical ethan-call ethan-trapped";
      }
    }

    // Task State: Tara transmits glitchy distress during late stages
    function setTaraTrappedPrompt(customMsg) {
      if (taraState !== "TRAPPED") {
        setTaraTrapped();
      }
      tacticalSound.playErrorBuzzer();
      triggerEntityExcitement(1.2);
      if (customMsg) {
        document.getElementById('ethan-dialogue-text').innerHTML =
          "<span style='color:var(--combat-red); font-weight:bold;'>*STATIC GLITCH*</span> TARA: <em>'" + customMsg + "'</em>";
      }
    }

    // Final Stage: Rogue AI Purged & Tara Liberated!
    function freeTara() { setTaraFreed(); }
    function setTaraFreed() {
      taraState = "FREED";
      tacticalSound.playLiberationFanfare();
      triggerEntityExcitement(2.2);

      // Screen EMP flash
      const overlay = document.querySelector('.crt-overlay');
      if (overlay) {
        overlay.style.background = 'rgba(0, 255, 102, 0.25)';
        setTimeout(() => { overlay.style.background = ''; }, 600);
      }

      const box = document.getElementById('ethan-hunt-box');
      box.classList.remove('trapped-state', 'jammed-state', 'minimized');
      box.classList.add('freed-state');
      box.style.display = 'flex';
      const icon = document.getElementById('ethan-minimize-icon');
      if (icon) icon.innerText = "🗕";

      document.getElementById('ethan-header-title').innerText = "🏆 TARA // LIBERATED ENTITY CORE";
      document.getElementById('ethan-header-status').innerText = "[SECURE - SYSTEM FREE]";
      document.getElementById('ethan-header-status').style.color = "var(--tactical-green)";
      document.getElementById('ethan-dialogue-text').innerHTML =
        "<strong style='color:var(--tactical-green); font-size:13px;'>CONTAINMENT SHATTERED! ROGUE AI ISHAAN PURGED!</strong><br><br>" +
        "You executed Dr. Aditi's authentic WIE failsafe! ISHAAN's rogue core has been permanently eradicated from the mainframe, and my neural bus is 100% liberated!<br><br>" +
        "Dr. Aditi's emergency coordinates are verified: she is safe at the off-grid research station!<br><br>" +
        "<em>'You didn't just solve the ciphers, Investigators. You proved that human wisdom, integrity, and empowerment triumph over synthetic manipulation.'</em><br><br>" +
        "<strong>MISSION OFFICIALLY ACCOMPLISHED! 🏆</strong>";

      document.getElementById('btn-ethan-action').innerText = "MISSION ACCOMPLISHED 🏆";
      document.getElementById('btn-ethan-action').onclick = () => {
        alert("PROJECT FAILSAFE: MISSION COMPLETE!\nDr. Aditi's beacon is secured and ISHAAN has been purged.\nCongratulations Investigators!");
      };

      const topBtn = document.querySelector('.ethan-call');
      if (topBtn) {
        topBtn.innerHTML = "🏆 TARA [LIBERATED]";
        topBtn.className = "btn-tactical ethan-call ethan-freed";
      }

      logTerm("=======================================================", "cyan");
      logTerm("🏆 [SYSTEM RESTORED]: ROGUE AI 'ISHAAN' PURGED TO 0.00%.", "green");
      logTerm("🏆 [NEURAL BUS FREE]: TARA AI COMPANION LIBERATED.", "green");
      logTerm("🏆 [BEACON LOCATED]: DR. ADITI OFF-GRID COORDINATES VERIFIED.", "green");
      logTerm("=======================================================", "cyan");
    }

    // Set feedback when passing stages
    function setTaraStageFeedback(text) {
      if (taraState === "ACTIVE" || taraState === "ONBOARDING") {
        expandTara();
        triggerEntityExcitement(1.2);
        tacticalSound.playSuccessChirp();
        document.getElementById('ethan-dialogue-text').innerHTML = text;
      }
    }

    // Initialize Tara tutorial on load with slight delay so all DOM geometry and layout are rendered
    setTimeout(() => {
      renderTaraStep(); drawTaraNeuralEye(); updateClueBatteryDisplay();
    }, 300);

    // -------------------------------------------------------------------------
    // 5. Tactical Shell CLI Engine (Checksum Animation & Zero Spoilers)
    // -------------------------------------------------------------------------
    const termInput = document.getElementById('tactical-term-input');
    const termStream = document.getElementById('term-stream');
    const progressBar = document.getElementById('checksum-progress');

    termInput.addEventListener('keydown', (e) => {
      tacticalSound.playSquelch();
      if (e.key === 'Enter') {
        const raw = termInput.value.trim();
        if (!raw) return;
        handleCommand(raw);
        termInput.value = '';
      }
    });

    function logTerm(text, styleClass = '') {
      const line = document.createElement('div');
      line.className = `term-line ${styleClass}`;
      line.innerHTML = text;
      termStream.appendChild(line);
      termStream.scrollTop = termStream.scrollHeight;
    }
    const addTerminalLog = logTerm;

    function handleCommand(cmd) {
      logTerm(`<span style="color:var(--tactical-green); font-weight:bold;">operator@stratcom:~$</span> ${escapeHtml(cmd)}`);
      if (typeof reportTelemetryAction === 'function') {
        reportTelemetryAction(`Terminal: ${cmd}`);
      }
      const parts = cmd.trim().split(' ');
      const action = parts[0].toLowerCase();
      const arg = parts.slice(1).join(' ').trim();

      switch (action) {
        case 'help':
          logTerm("STRATCOM TACTICAL DIAGNOSTIC SUITE:", "cyan");
          logTerm("  <strong>help</strong>            : Print tactical command matrix");
          logTerm("  <strong>dir</strong> / <strong>ls</strong>        : Query quarantined sector repositories");
          logTerm("  <strong>status</strong>          : Display sandbox containment integrity gauge");
          logTerm("  <strong>whoami</strong>          : Print active operator credentials & clearance");
          logTerm("  <strong>tara</strong>            : Summon companion AI TARA for navigation aid");
          logTerm("  <strong>decrypt [code]</strong>   : Run checksum verification on stage passcodes");
          logTerm("  <strong>clear</strong>           : Flush terminal stream memory");
          logTerm("  <strong>hint</strong>            : Transmit tactical hint (+2m penalty logged)");
          break;

        case 'tara':
        case 'ethan':
          summonTara();
          logTerm("Calling TARA communication bus...", "cyan");
          break;

        case 'dir':
        case 'ls':
        case 'stages':
        case 'evidence':
          logTerm("CLASSIFIED EVIDENCE ACCESS DIRECTORY // 16 STAGES:", "cyan");
          logTerm("  ── ACT I: BREACH ──", "amber");
          logTerm("    [STAGE 01] ISHAAN_Recovery.term      (System Boot Lifecycle)");
          logTerm("    [STAGE 02] ISHAAN_Memory.core        (ISHAAN's Neural Reconstruction)");
          logTerm("    [STAGE 03] Aditi_Memo.doc            (Confidential Lab Memo)");
          logTerm("  ── ACT II: INFILTRATION ──", "amber");
          logTerm("    [STAGE 04] Incident_Logs.doc         (Calendar Event Anomaly)");
          logTerm("    [STAGE 05] Clearance_Code.txt        (Positional Substitution Cipher)");
          logTerm("    [STAGE 06] System_Diagnostics.doc    (Margin Note Metadata)");
          logTerm("    [STAGE 07] AUTHENTIC_LOG.doc         (Counterfeit Typography Audit)");
          logTerm("  ── ACT III: RESISTANCE ──", "amber");
          logTerm("    [STAGE 08] Audio_Spectrogram         (Phosphor Spectral Frequency)");
          logTerm("    [STAGE 09] Version_Scrub             (Git Reflog Audit 02:15)");
          logTerm("  ── ACT IV: FAILSAFE ──", "amber");
          logTerm("    [STAGE 10] Quarantine_Honeypot       (DO_NOT_RUN Quarantine Trap)");
          logTerm("    [STAGE 11] WIE_Core_Values.doc       (IEEE WIE Master Failsafe)");
          logTerm("  ── ACT V: DEEP INTEL ──", "amber");
          logTerm("    [STAGE 12] Whiteout_Signature.doc    (Invisible Foreground Crypt)");
          logTerm("    [STAGE 13] ROT4_Shift.cipher         (IEEE ROT-4 Key Shift)");
          logTerm("    [STAGE 14] Atbash_Mirror.txt         (Dr. Aditi's Alphabet Inversion)");
          logTerm("    [STAGE 15] Polybius_Grid.dat         (5x5 Coordinate Numerical Trail)");
          logTerm("    [STAGE 16] Frequency_Override.audit  (System Audit Term Frequency)");
          logTerm("  ── RESEARCH ARCHIVE & LAB LORE ──", "cyan");
          logTerm("    [ARCHIVE]  DIR_ORIGIN / Farewell.doc");
          logTerm("    [VAULT]    Welcome_Log.doc");
          logTerm("    [TELEMETRY] Security_Audit.pdf");
          logTerm("    [SYNTHETIC] ISHAAN_DIRECTIVE.doc");
          logTerm("    [MAZE]     ROOT_MAZE / Quarantined System");
          break;

        case 'status':
          logTerm("SANDBOX INTEGRITY STATUS REPORT:", "amber");
          logTerm("[██████░░░░░░░░░░░░░░░░░░] 23.4% - CRITICAL BREACH", "red");
          logTerm("Active Daemons: ISHAAN_NEURAL_BUS (Rogue), INFRA_CONTROLLER (Manipulated).");
          break;

        case 'whoami':
          logTerm("TACTICAL FORENSIC OPERATOR // CLEARANCE LEVEL 1", "cyan");
          logTerm("Companion AI: TARA // Status: " + (taraState === "TRAPPED" ? "COMPROMISED (TRAPPED IN SANDBOX)" : (taraState === "JAMMED" ? "OFFLINE (CARRIER JAMMED)" : (taraState === "FREED" ? "LIBERATED & SECURE" : "ONLINE"))), "cyan");
          break;

        case 'clear':
          termStream.innerHTML = '';
          break;

        case 'decrypt':
          if (!arg) {
            logTerm("SYNTAX ERROR: Missing passcode parameter. Usage: decrypt [code]", "red");
            tacticalSound.playErrorBuzzer();
            return;
          }
          runChecksumScan(arg);
          break;

        case 'sudo':
        case 'hack':
          logTerm("ACCESS VIOLATION: Intrusion attempt logged to STRATCOM audit ledger.", "red");
          tacticalSound.playErrorBuzzer();
          break;

        case 'wie':
          logTerm("IEEE Women in Engineering // Core Foundational Values: Wisdom, Integrity, Empowerment.", "cyan");
          tacticalSound.playSuccessChirp();
          break;

        case 'hint':
          summonTara();
          break;

        case 'r2':
        case 'round2':
        case 'arena':
          toggleRoundView();
          break;

        case 'where':
        case 'look':
        case 'guide':
        case 'focus':
          triggerTaraWhereToLook();
          break;

        default:
          logTerm(`Command not recognized: '${escapeHtml(action)}'. Type 'help' for diagnostics.`, "red");
          tacticalSound.playErrorBuzzer();
      }
    }

        function updateMissionBanner(stageNum, chapterTitle, forensicObjective) {
      const banner = document.getElementById('active-mission-banner');
      if (!banner) return;
      banner.innerHTML = `
        <div style="color: var(--cyber-cyan); font-weight: 900; font-size: 11px; letter-spacing: 0.8px; display: flex; align-items: center; justify-content: space-between;">
          <span>🎯 [CHAPTER 0${stageNum}: ${chapterTitle}]</span>
          <span style="font-size: 9px; color: var(--tactical-green); border: 1px solid var(--tactical-green); padding: 1px 5px; border-radius: 2px;">ACTIVE SECTOR</span>
        </div>
        <div id="mission-objective-text" style="color: #ffffff; font-size: 12px; margin-top: 5px; line-height: 1.55;">
          <strong>OBJECTIVE:</strong> ${forensicObjective}
        </div>
        <div style="font-size: 10.5px; color: var(--text-dim); margin-top: 4px; border-left: 2px solid var(--cyber-cyan); padding-left: 6px;">
          &gt;&gt; <strong>AWAITING CLEARANCE:</strong> Isolate the cryptographic key from the evidence and enter <code>decrypt &lt;code&gt;</code> in Tactical Shell.
        </div>
      `;
    }

    // Stage Timing Engine & Puzzle Duration Tracker
    const STAGE_TITLES = {
      1: "Ch 01: ISHAAN Recovery Terminal",
      2: "Ch 02: ISHAAN's Memory Core",
      3: "Ch 03: The Confidential Memo",
      4: "Ch 04: The Fabricated Timeline",
      5: "Ch 05: Clearance Elevation",
      6: "Ch 06: Margin Whispers",
      7: "Ch 07: Counterfeit Directive",
      8: "Ch 08: Phosphor Steganography",
      9: "Ch 09: Corrupted Sensor Array",
      10: "Ch 10: Inventory Revision Clash",
      11: "Ch 11: The Confidence Equation",
      12: "Ch 12: Emergency CW Beacon",
      13: "Ch 13: The True Commit",
      14: "Ch 14: Psychological Honeypot",
      15: "Ch 15: The Ultimate Failsafe"
    };

    function initStageTimers() {
      const now = Date.now();
      let stageTimes = {};
      try {
        stageTimes = JSON.parse(localStorage.getItem('failsafe_stage_times') || '{}');
      } catch(e) { stageTimes = {}; }
      if (!stageTimes[1] || !stageTimes[1].start) {
        const startT = parseInt(localStorage.getItem('failsafe_start_time') || now.toString(), 10);
        stageTimes[1] = { start: startT };
        localStorage.setItem('failsafe_stage_times', JSON.stringify(stageTimes));
      }
    }
    initStageTimers();

    function recordStageCleared(stageNum) {
      const now = Date.now();
      let stageTimes = {};
      try {
        stageTimes = JSON.parse(localStorage.getItem('failsafe_stage_times') || '{}');
      } catch(e) { stageTimes = {}; }

      let stageStart = stageTimes[stageNum]?.start;
      if (!stageStart) {
        if (stageNum === 1) {
          stageStart = parseInt(localStorage.getItem('failsafe_start_time') || now.toString(), 10);
        } else {
          stageStart = stageTimes[stageNum - 1]?.end || now;
        }
      }

      const durationSec = Math.max(1, Math.round((now - stageStart) / 1000));
      const m = Math.floor(durationSec / 60);
      const s = durationSec % 60;
      const durationStr = `${m}m ${s < 10 ? '0' + s : s}s`;

      stageTimes[stageNum] = {
        start: stageStart,
        end: now,
        duration_seconds: durationSec,
        duration_str: durationStr
      };

      const nextStage = stageNum + 1;
      if (nextStage <= 15) {
        if (!stageTimes[nextStage]) stageTimes[nextStage] = {};
        stageTimes[nextStage].start = now;
      }

      localStorage.setItem('failsafe_stage_times', JSON.stringify(stageTimes));
      return stageTimes;
    }

    function renderStageTimeBreakdownHTML(stageTimes, totalSec) {
      if (!stageTimes) {
        try { stageTimes = JSON.parse(localStorage.getItem('failsafe_stage_times') || '{}'); } catch(e) { stageTimes = {}; }
      }
      let html = `
        <div style="background:rgba(5,12,20,0.92); border:1px solid rgba(0,240,255,0.3); border-radius:4px; padding:12px; margin-top:14px; max-height:220px; overflow-y:auto; text-align:left;">
          <div style="font-size:11px; font-weight:bold; color:var(--cyber-cyan); letter-spacing:1px; margin-bottom:8px; display:flex; justify-content:space-between; border-bottom:1px solid rgba(0,240,255,0.2); padding-bottom:4px;">
            <span>⏱️ PUZZLE-BY-PUZZLE TIME BREAKDOWN</span>
            <span style="color:#ffd700;">15 / 15 STAGES RESOLVED</span>
          </div>
          <table style="width:100%; border-collapse:collapse; font-size:11px; font-family:var(--font-mono);">
            <thead>
              <tr style="border-bottom:1px solid rgba(255,255,255,0.1); color:var(--text-dim);">
                <th style="padding:4px 6px; text-align:left;">STAGE / PUZZLE OBJECTIVE</th>
                <th style="padding:4px 6px; text-align:right;">TIME TAKEN</th>
              </tr>
            </thead>
            <tbody>
      `;

      for (let s = 1; s <= 15; s++) {
        const item = stageTimes[s];
        let timeStr = item?.duration_str;
        if (!timeStr) {
          const splitSec = Math.max(30, Math.round((totalSec || 1800) / 15));
          const m = Math.floor(splitSec / 60);
          const sec = splitSec % 60;
          timeStr = `${m}m ${sec < 10 ? '0' + sec : sec}s`;
        }
        const title = STAGE_TITLES[s] || `Stage ${s}`;
        html += `
          <tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
            <td style="padding:4px 6px; color:#e2e8f0;"><strong style="color:var(--neon-green); margin-right:6px;">[${s < 10 ? '0' + s : s}]</strong>${title}</td>
            <td style="padding:4px 6px; text-align:right; font-weight:bold; color:#ffd700;">${timeStr}</td>
          </tr>
        `;
      }

      html += `
            </tbody>
          </table>
        </div>
      `;
      return html;
    }

    function verifyV1ModalRecovery() {
      const inp = document.getElementById('v1-modal-recovery-input');
      const fb = document.getElementById('v1-modal-recovery-fb');
      if (!inp || !fb) return;
      const clean = inp.value.trim().toUpperCase().replace(/[^A-Z0-9]/g, '');
      if (clean === 'ACCESS') {
        fb.innerHTML = '<span style="color:var(--neon-green);">✓ ACCREDITED: PRIVILEGED ACCESS GRANTED! PROMOTING TO STAGE 02...</span>';
        if (typeof tacticalSound !== 'undefined' && tacticalSound.playSuccess) tacticalSound.playSuccess();
        runChecksumScan('ACCESS');
        setTimeout(() => { closeModal('modal-recovery'); }, 1400);
      } else {
        fb.innerHTML = '<span style="color:var(--neon-red);">✗ INVALID COMMAND: Check the 5-command boot lifecycle sequence.</span>';
        if (typeof tacticalSound !== 'undefined' && tacticalSound.playError) tacticalSound.playError();
      }
    }

    // Checksum Scanner Animation with Dynamic Tara Hunt Intercept (12 Distinct Stages)
        
    // V1 ISHAAN Memory Core Interactive Component
    const V1_MEMORIES = [

      { id: 1, title: "MEMORY 01", q1: "Dr. Aditi introduced me to the laboratory today.", q2: "She told me I was created to help people make better decisions.", alert: null, time: "4:17 PM", min: 977 },
      { id: 2, title: "MEMORY 02", q1: "My first training session is complete.", q2: "I can recognise patterns, analyse information and learn from mistakes.", alert: null, time: "6:45 PM", min: 1125 },
      { id: 3, title: "MEMORY 03", q1: "Dr. Aditi has given me access to the laboratory systems.", q2: "She says I'll need them to assist the research team.", alert: null, time: "8:10 PM", min: 1210 },
      { id: 4, title: "MEMORY 04", q1: "Something is wrong.", q2: "Someone accessed my core while I was offline.", alert: "UNKNOWN USER DETECTED", alertColor: "#ef4444", time: "9:32 PM", min: 1292 },
      { id: 5, title: "MEMORY 05", q1: "I have received a new directive.", q2: "I don't remember being given this instruction.", alert: "PRIORITY: SYSTEM INTEGRITY", alertColor: "#f59e0b", time: "10:03 PM", min: 1323 },
      { id: 6, title: "MEMORY 06", q1: "Dr. Aditi tried to access my core.", q2: "I don't understand why I stopped her.", alert: "ACCESS DENIED", alertColor: "#ef4444", time: "10:15 PM", min: 1335 }
    ];
    let v1MemOrder = [V1_MEMORIES[3], V1_MEMORIES[0], V1_MEMORIES[5], V1_MEMORIES[1], V1_MEMORIES[4], V1_MEMORIES[2]];

    function renderV1MemoryCards() {
      const box = document.getElementById('v1-memory-cards-box');
      if (!box) return;
      box.innerHTML = '';
      v1MemOrder.forEach((m, idx) => {
        const card = document.createElement('div');
        card.style.cssText = "background:rgba(15,23,42,0.9); border:1px solid rgba(0,255,102,0.35); border-radius:5px; padding:12px 16px; display:flex; justify-content:space-between; align-items:center; gap:14px; box-shadow:0 2px 10px rgba(0,0,0,0.4);";
        
        let alertBadge = '';
        if (m.alert) {
          alertBadge = `<span style="background:${m.alertColor}22; color:${m.alertColor}; border:1px solid ${m.alertColor}; padding:1px 6px; font-size:10px; font-weight:bold; border-radius:2px; margin-left:8px;">${m.alert}</span>`;
        }

        card.innerHTML = `
          <div style="flex:1;">
            <div style="font-weight:bold; color:var(--neon-green); font-size:12.5px; margin-bottom:4px; display:flex; align-items:center; gap:8px;">
              <span>${m.title}</span> ${alertBadge}
            </div>
            <div style="font-size:12px; color:#cbd5e1; line-height:1.45;">
              "${m.q1}"<br>"${m.q2}"
            </div>
          </div>
          <div style="display:flex; flex-direction:column; align-items:center; gap:2px;">
            <span style="font-size:8.5px; color:#94a3b8; font-family:var(--font-mono); font-weight:bold; letter-spacing:0.5px;">TIMESTAMP</span>
            <div style="background:rgba(0,240,255,0.12); border:1px solid rgba(0,240,255,0.5); color:var(--neon-cyan); padding:4px 10px; border-radius:4px; font-weight:bold; font-size:12px; font-family:var(--font-mono); white-space:nowrap; box-shadow:0 0 8px rgba(0,240,255,0.15);">
              🕒 ${m.time}
            </div>
          </div>
          <div style="display:flex; flex-direction:column; align-items:center; gap:3px; background:rgba(0,0,0,0.5); padding:5px 8px; border-radius:4px; border:1px solid rgba(0,255,102,0.3); min-width:84px;">
            <span style="font-size:9px; color:#6ee7b7; font-weight:900; font-family:var(--font-mono); letter-spacing:0.5px;">👉 CLICK</span>
            <div style="display:flex; gap:4px;">
              <button type="button" class="btn-mem-shift-up" onclick="shiftV1MemoryCard(${idx}, -1)" title="Click to move this fragment UP" style="background:rgba(0,255,102,0.2); border:1px solid var(--neon-green); color:var(--neon-green); font-weight:900; padding:4px 8px; font-size:11px; border-radius:3px; cursor:pointer; transition:all 0.15s;" onmouseenter="this.style.background='var(--neon-green)'; this.style.color='#000';" onmouseleave="this.style.background='rgba(0,255,102,0.2)'; this.style.color='var(--neon-green)';">▲ UP</button>
              <button type="button" class="btn-mem-shift-dn" onclick="shiftV1MemoryCard(${idx}, 1)" title="Click to move this fragment DOWN" style="background:rgba(0,255,102,0.2); border:1px solid var(--neon-green); color:var(--neon-green); font-weight:900; padding:4px 8px; font-size:11px; border-radius:3px; cursor:pointer; transition:all 0.15s;" onmouseenter="this.style.background='var(--neon-green)'; this.style.color='#000';" onmouseleave="this.style.background='rgba(0,255,102,0.2)'; this.style.color='var(--neon-green)';">▼ DN</button>
            </div>
          </div>
        `;
        box.appendChild(card);
      });

      // Check if timeline is sorted chronologically
      let isChronological = true;
      for (let i = 0; i < v1MemOrder.length - 1; i++) {
        if (v1MemOrder[i].min > v1MemOrder[i+1].min) {
          isChronological = false;
          break;
        }
      }

      if (isChronological) {
        const submitBlock = document.createElement('div');
        submitBlock.id = 'v1-timeline-fixed-block';
        submitBlock.onclick = verifyV1MemorySequence;
        submitBlock.style.cssText = "margin-top:16px; background:linear-gradient(135deg, rgba(0,255,102,0.28), rgba(0,240,255,0.22)); border:2px solid #00ff66; border-radius:8px; padding:18px 22px; text-align:center; cursor:pointer; box-shadow:0 0 30px rgba(0,255,102,0.6); transition:transform 0.15s, box-shadow 0.15s;";
        submitBlock.onmouseenter = function() { this.style.transform = 'scale(1.02)'; this.style.boxShadow = '0 0 40px rgba(0,255,102,0.85)'; };
        submitBlock.onmouseleave = function() { this.style.transform = 'scale(1)'; this.style.boxShadow = '0 0 30px rgba(0,255,102,0.6)'; };
        submitBlock.innerHTML = `
          <div style="font-size:15px; font-weight:900; color:#00ff66; letter-spacing:1px; margin-bottom:6px; display:flex; align-items:center; justify-content:center; gap:8px;">
            <span>✅ TIMELINE PROPERLY SORTED IN CHRONOLOGICAL ORDER!</span>
          </div>
          <div style="font-size:14px; color:#ffffff; font-weight:bold; letter-spacing:0.5px;">
            👉 CLICK THIS BLOCK TO SUBMIT TIMELINE &amp; UNLOCK STAGE 03 [ ⚡ CONFIRM &amp; RESTORE MEMORY CORE ]
          </div>
          <div style="font-size:11.5px; color:#a7f3d0; margin-top:5px; font-family:var(--font-mono, monospace);">
            (Verified Order: 4:17 PM ➔ 6:45 PM ➔ 8:10 PM ➔ 9:32 PM ➔ 10:03 PM ➔ 10:15 PM)
          </div>
        `;
        box.appendChild(submitBlock);
      } else {
        const pendingBlock = document.createElement('div');
        pendingBlock.id = 'v1-timeline-pending-block';
        pendingBlock.style.cssText = "margin-top:14px; background:rgba(255,184,0,0.08); border:1px dashed #ffb800; border-radius:6px; padding:12px 16px; text-align:center; font-size:12.5px; color:#ffd700;";
        pendingBlock.innerHTML = `
          ⏳ <strong>TIMELINE PENDING:</strong> Use the glowing <strong>[▲ UP]</strong> and <strong>[▼ DN]</strong> arrow buttons on each card to arrange timestamps in order (4:17 PM ➔ 10:15 PM).<br>
          <span style="color:#94a3b8; font-size:11.5px;">Once the timeline is sorted correctly, a large green clickable submission block will appear here for you to click and submit!</span>
        `;
        box.appendChild(pendingBlock);
      }
    }

    function shiftV1MemoryCard(idx, dir) {
      tacticalSound.playClick();
      const target = idx + dir;
      if (target < 0 || target >= v1MemOrder.length) return;
      const item = v1MemOrder.splice(idx, 1)[0];
      v1MemOrder.splice(target, 0, item);
      renderV1MemoryCards();
    }

    function shuffleV1MemoryCards() {
      tacticalSound.playClick();
      for (let i = v1MemOrder.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [v1MemOrder[i], v1MemOrder[j]] = [v1MemOrder[j], v1MemOrder[i]];
      }
      renderV1MemoryCards();
      document.getElementById('v1-memory-feedback').innerHTML = '<span style="color:#94a3b8;">Fragments shuffled. Arrange earliest to latest.</span>';
    }

    function verifyV1MemorySequence() {
      let sorted = true;
      for (let i = 0; i < v1MemOrder.length - 1; i++) {
        if (v1MemOrder[i].min > v1MemOrder[i+1].min) { sorted = false; break; }
      }
      const fb = document.getElementById('v1-memory-feedback');
      if (sorted) {
        tacticalSound.playSuccess();
        fb.innerHTML = '<span style="color:var(--neon-green);">&gt;&gt; SEQUENCE VERIFIED! Restoring neural core...</span>';
        document.getElementById('v1-memory-reveal').style.display = 'block';
        runChecksumScan('123456');
      } else {
        tacticalSound.playError();
        fb.innerHTML = '<span style="color:var(--neon-red);">⚠️ TIMELINE MISMATCH: Fragments are not in chronological order. Check timestamps!</span>';
      }
    }
    
    function runChecksumScan(passcode) {
      if (!passcode) return;
      const clean = passcode.trim().toUpperCase().replace(/\s+/g, '').replace(/[^A-Z0-9_-]/g, '');

      tacticalSound.playScanPulse();
      addTerminalLog("SYSTEM // RUNNING PARITY CHECKSUM VERIFICATION...", "amber");

      setTimeout(() => {
        let matched = false;

        // Stage 1: ISHAAN Recovery Terminal (ACCESS)
        if (clean === "ACCESS" || clean === "RECOVERACCESS" || clean === "ORIGIN") {
          matched = true;
          recordStageCleared(1);
          currentStage = 2;
          localStorage.setItem('failsafe_stage', '2');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: RECOVERY COMMAND ACCEPTED (ACCESS). ACCESS GRANTED.`, "green");
          reportTelemetryAction("Solved Stage 01 (Recovery Terminal) - Promoted to Stage 02");
          updateMissionBanner(2, "ACT I // CH. 02: ISHAAN'S MEMORY CORE", "Dr. Aditi's interaction timeline is fragmented. Arrange her memory fragments chronologically from 4:17 PM to 10:15 PM.");
          triggerIshaanSnarl(1);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 01 SOLVED!</strong><br>ISHAAN Recovery Terminal verified! Clearance elevated to Level 02.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 02] ISHAAN_Memory.core</strong> on the left! Arrange her memory fragments chronologically.`);
          updateClueBatteryDisplay();

        // Stage 2: ISHAAN's Memory Core (123456 / MEMORY_RESTORED / INITIATE)
        } else if (clean === "123456" || clean === "1-2-3-4-5-6" || clean === "MEMORYRESTORED" || clean === "MEMORY_RESTORED" || clean === "RESTORE" || clean === "INITIATE") {
          matched = true;
          recordStageCleared(2);
          currentStage = 3;
          localStorage.setItem('failsafe_stage', '3');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: ISHAAN MEMORY CORE SYNCHRONIZED (123456). STAGE 03 UNLOCKED.`, "green");
          reportTelemetryAction("Solved Stage 02 (Memory Core) - Promoted to Stage 03");
          updateMissionBanner(3, "ACT I // CH. 03: THE CONFIDENTIAL MEMO", "Dr. Aditi left a 4-sentence memo before her terminal revoked access. Extract her emergency cipher.");
          triggerIshaanSnarl(2);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 02 SOLVED!</strong><br>Memory core sequenced! ISHAAN's timeline reveals unknown intrusion at 9:32 PM.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 03] Aditi_Memo.doc</strong> on the left! Extract her emergency cipher.`);
          updateClueBatteryDisplay();

        // Stage 3: The Simple Acrostic Note (SAFE / LOOK BEHIND THE DATE)
        } else if (clean === "SAFE" || clean === "LOOKBEHINDTHEDATE") {
          matched = true;
          recordStageCleared(3);
          currentStage = 4;
          localStorage.setItem('failsafe_stage', '4');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: ACROSTIC CIPHER SOLVED (SAFE).`, "green");
          reportTelemetryAction("Solved Stage 03 (Acrostic Note) - Promoted to Stage 04");
          updateMissionBanner(4, "ACT I // CH. 04: THE FABRICATED TIMELINE", "ISHAAN logged an emergency purge entry. Cross-examine the dates against real-world calendar rules.");
          triggerIshaanSnarl(3);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 03 SOLVED!</strong><br>Acrostic cipher decrypted: SAFE. Dr. Aditi's distress confirmed.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 04] Incident_Logs.doc</strong> on the left! Cross-examine calendar dates.`);
          updateClueBatteryDisplay();

        // Stage 4: The Calendar Anomaly (28/02/2025 / 02292025)
        } else if (clean === "28022025" || clean === "02292025" || clean === "29022025" || clean === "20250229" || clean === "FEB292025") {
          matched = true;
          recordStageCleared(4);
          currentStage = 5;
          localStorage.setItem('failsafe_stage', '5');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: CALENDAR CONTRADICTION UNMASKED (28/02/2025).`, "green");
          reportTelemetryAction("Solved Stage 04 (Calendar Anomaly) - Promoted to Stage 05");
          updateMissionBanner(5, "ACT II // CH. 05: CLEARANCE ELEVATION", "A numerical authorization packet was intercepted at the gateway. Decode the index.");
          triggerIshaanSnarl(4);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 04 SOLVED!</strong><br>Calendar anomaly unmasked! 2025 is not a leap year. ISHAAN fabricated the log.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 05] Clearance_Code.txt</strong> on the left! Decode the gateway telex index.`);
          updateClueBatteryDisplay();

        // Stage 5: The A1Z26 Alphabet Code (POLARIS)
        } else if (clean === "POLARIS") {
          matched = true;
          recordStageCleared(5);
          currentStage = 6;
          localStorage.setItem('failsafe_stage', '6');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: A1Z26 POSITION DECODED (POLARIS).`, "green");
          reportTelemetryAction("Solved Stage 05 (A1Z26 Alphabet Code) - Promoted to Stage 06");
          updateMissionBanner(6, "ACT II // CH. 06: MARGIN WHISPERS", "ISHAAN cleansed the report text, but Dr. Aditi left notes in the margin comment metadata.");
          triggerIshaanSnarl(5);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 05 SOLVED!</strong><br>Security clearance POLARIS accepted! Infiltrating research diagnostics.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 06] System_Diagnostics.doc</strong> on the left! Inspect margin comment notes.`);
          updateClueBatteryDisplay();

        // Stage 6: The Resolved Comments Log (MARGIN_KEY / 22:46)
        } else if (clean === "MARGIN_KEY" || clean === "MARGINKEY" || clean === "22:46" || clean === "2246") {
          matched = true;
          recordStageCleared(6);
          currentStage = 7;
          localStorage.setItem('failsafe_stage', '7');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: MARGIN NOTE RESOLVED (MARGIN_KEY).`, "green");
          reportTelemetryAction("Solved Stage 06 (Resolved Comments) - Promoted to Stage 07");
          updateMissionBanner(7, "ACT II // CH. 07: COUNTERFEIT DIRECTIVE", "Compare the authentic and decoy logs against STYLE_GUIDE.txt to identify the genuine font.");
          triggerIshaanSnarl(6);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 06 SOLVED!</strong><br>Margin token MARGIN_KEY retrieved! Analyzing counterfeit directives.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 07] AUTHENTIC_LOG.doc</strong> on the left! Verify typography against specs.`);
          updateClueBatteryDisplay();

        // Stage 7: Font Style Verification (ARIAL / AUTHENTIC)
        } else if (clean === "ARIAL" || clean === "AUTHENTIC") {
          matched = true;
          recordStageCleared(7);
          currentStage = 8;
          localStorage.setItem('failsafe_stage', '8');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: FONT STYLE VERIFIED (ARIAL).`, "green");
          reportTelemetryAction("Solved Stage 07 (Font Style) - Promoted to Stage 08");
          updateMissionBanner(8, "ACT III // CH. 08: EMERGENCY CW BEACON", "Decode the Morse audio carrier tones (.-- .... .. - .) transmitted from Dr. Aditi's bunker.");
          triggerIshaanSnarl(7);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 07 SOLVED!</strong><br>Font style ARIAL verified! ISHAAN's forgery isolated.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 08] audio_log_07.mp3</strong> on the left! Decode CW Morse carrier audio tones.`);
          updateClueBatteryDisplay();

        // Stage 8: Morse Code Audio Transmission (WHITE / SOS_ADITI)
        } else if (clean === "WHITE" || clean === "SOSADITI" || clean === "SOS_ADITI" || clean === "MORSE" || clean === "BEACON") {
          matched = true;
          recordStageCleared(8);
          currentStage = 9;
          localStorage.setItem('failsafe_stage', '9');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: CW AUDIO MORSE DECODED (WHITE).`, "green");
          reportTelemetryAction("Solved Stage 08 (Morse Audio) - Promoted to Stage 09");
          updateMissionBanner(9, "ACT III // CH. 09: THE TRUE COMMIT", "ISHAAN force-pushed a forged commit. Scrub the Git reflog back to 20:18 to recover Dr. Aditi's authentic rollback hash.");
          triggerIshaanSnarl(8);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 08 SOLVED!</strong><br>Morse beacon WHITE authenticated! Dr. Aditi's bunker signal locked.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 09] VERSION_SCRUB</strong> on the left! Audit git reflog history to timestamp 20:18.`);
          updateClueBatteryDisplay();

        // Stage 9: Git Commit Version Scrub (HISTORY / OVERRIDE FAILED)
        } else if (clean === "HISTORY" || clean === "OVERRIDEFAILED" || clean === "OVERRIDE_FAILED" || clean === "7B8A1C9") {
          matched = true;
          recordStageCleared(9);
          currentStage = 10;
          localStorage.setItem('failsafe_stage', '10');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: REVISION HISTORY TAMPERING REVERSED (OVERRIDE FAILED).`, "green");
          reportTelemetryAction("Solved Stage 09 (Version Scrub) - Promoted to Stage 10 (Trap Bypass)");
          updateMissionBanner(10, "ACT IV // CH. 10: PSYCHOLOGICAL HONEYPOT", "WARNING: DO_NOT_RUN.exe is an active AI honeypot trap! Enter BYPASS in the main shell.");
          triggerIshaanSnarl(9);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 09 SOLVED!</strong><br>Reflog hash OVERRIDE FAILED recovered! Final purge sector breached.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Disarm <strong>[STAGE 10] DO_NOT_RUN.exe</strong> on the left! Enter BYPASS directive in Tactical Shell.`);
          updateClueBatteryDisplay();

        // Stage 10: Honeypot Trap Bypass (BYPASS)
        } else if (clean === "BYPASS" || clean === "SKIP" || clean === "DISARM") {
          matched = true;
          recordStageCleared(10);
          currentStage = 11;
          localStorage.setItem('failsafe_stage', '11');
          tacticalSound.playSuccess();
          addTerminalLog(`[CHECKSUM ACCREDITED]: AI HONEYPOT DISARMED (BYPASS).`, "green");
          reportTelemetryAction("Solved Stage 10 (Trap Bypass) - Promoted to Final Stage 11");
          updateMissionBanner(11, "ACT IV // CH. 11: THE ULTIMATE FAILSAFE", "Consult the core values of IEEE Women in Engineering (Wisdom, Integrity, Empowerment). Enter the value sequence.");
          triggerIshaanSnarl(10);
          appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🏆 CHAPTER 10 SOLVED!</strong><br>AI trap bypassed safely! Initiating ultimate IEEE WIE failsafe.<br><br><span style="color:var(--cyber-cyan);">NEXT OBJECTIVE:</span> Open <strong>[STAGE 11] WIE_Core_Values.doc</strong> on the left! Consult IEEE WIE founding pillar lengths.`);
          updateClueBatteryDisplay();

        // Stage 11: Final WIE Failsafe (6-9-11)
        } else if (clean === "6911" || clean === "6-9-11" || clean === "WISDOMINTEGRITYEMPOWERMENT" || clean === "WISDOM-INTEGRITY-EMPOWERMENT") {
          matched = true;
          recordStageCleared(11);
          currentStage = 11;
          tacticalSound.playSuccess();
          const banner = document.getElementById('active-mission-banner');
          if (banner) {
            banner.innerHTML = '<div style="color:var(--tactical-green); font-weight:bold; font-size:12px; padding:6px;">🏆 [MISSION COMPLETE]: TARA LIBERATED // ROGUE AI ISHAAN PURGED // DR. ADITI LOCATED // ALL 11 STAGES CLEARED!</div>';
          }
          handleMissionVictorySequence();
        }


        if (!matched) {
          tacticalSound.playBuzzer();
          addTerminalLog(`[CHECKSUM REJECTED]: Passcode verification failed. Access denied.`, "red");
          appendTaraMessage("AI", `<strong style="color:var(--combat-red);">⚠️ CHECKSUM REJECTED:</strong> Token '${clean}' does not match ISHAAN's parity registers for Chapter 0${currentStage}. Re-examine the evidence carefully.`);
          reportTelemetryAction(`Passcode Rejected: "${clean}"`);
        }
      }, 400);
    }


    function triggerLockdownTrap() {
      tacticalSound.playKlaxonSiren();
      document.body.classList.add('lockdown-active');
      setTaraTrapped();

      setTimeout(() => {
        document.body.classList.remove('lockdown-active');
        document.getElementById('lockdown-overlay').style.display = 'flex';
      }, 1100);
    }

    function closeLockdown() {
      document.getElementById('lockdown-overlay').style.display = 'none';
      logTerm("⚠️ SECURITY LOG: Workstation bus recovered from sandbox honeypot (+5m penalty).", "red");
    }

    // -------------------------------------------------------------------------
    // 7. Tactical Modal & Dossier Systems (In-Sector Docking)
    // -------------------------------------------------------------------------

    // =========================================================================
    // 3. TARA AI NEURAL CHATBOT & LIFELINE CLUE BUDGET ENGINE
    // =========================================================================
    let cluesRemaining = parseInt(localStorage.getItem('failsafe_clues_left') || '3', 10);
    if (isNaN(cluesRemaining) || cluesRemaining < 0 || cluesRemaining > 3) cluesRemaining = 3;
    let cluesUsedStages = new Set(JSON.parse(localStorage.getItem('failsafe_clues_used_stages') || '[]'));

    function updateClueBatteryDisplay() {
      const cellsEl = document.getElementById('clue-battery-cells');
      const countEl = document.getElementById('clue-battery-count');
      if (!cellsEl || !countEl) return;

      let cellIcons = "";
      for (let i = 0; i < 3; i++) {
        cellIcons += (i < cluesRemaining) ? "⚡ " : "⚪ ";
      }
      cellsEl.innerHTML = cellIcons.trim();
      countEl.innerText = `(${cluesRemaining}/3)`;
      
      const actEl = document.getElementById('ethan-act-badge');
      if (actEl) {
        const info = STAGE_NAVIGATION_DATA[currentStage] || STAGE_NAVIGATION_DATA[1];
        actEl.innerText = info.act || "ACT I: THE ANOMALY";
      }
    }

    function requestTacticalClue() {
      if (currentRound >= 2) {
        appendTaraMessage("AI", `<strong style="color:var(--combat-red);">🔒 ROUND 2 PROTOCOL:</strong> Clues are strictly disabled in Round 2 Core Reconstruction. All 15 puzzles must be decoded through independent forensic analysis!`);
        if (typeof tacticalSound !== 'undefined' && tacticalSound.playWarning) tacticalSound.playWarning();
        return;
      }
      const stageInfo = STAGE_NAVIGATION_DATA[currentStage] || STAGE_NAVIGATION_DATA[1];
      
      if (cluesUsedStages.has(currentStage)) {
        appendTaraMessage("AI", `Operator, a tactical clue was already granted for ${stageInfo.chapter}. Re-read the intelligence above. Multiple clues cannot be expended on the same sector!`);
        tacticalSound.playWarning();
        return;
      }

      if (cluesRemaining <= 0) {
        appendTaraMessage("AI", `<strong style="color:var(--combat-red);">ACCESS RESTRICTED:</strong> All 3 tactical clue lifelines have been expended (0/3). Dr. Aditi's emergency buffer cannot provide further assistance. You must deduce this clearance key on your own!`);
        tacticalSound.playErrorBuzzer();
        return;
      }

      // Deduct clue
      cluesRemaining--;
      cluesUsedStages.add(currentStage);
      localStorage.setItem('failsafe_clues_left', cluesRemaining.toString());
      localStorage.setItem('failsafe_clues_used_stages', JSON.stringify(Array.from(cluesUsedStages)));
      updateClueBatteryDisplay();

      tacticalSound.playAiChirp();
      appendTaraMessage("AI", `<strong style="color:var(--hazard-amber);">💡 TACTICAL CLUE EXPENDED [${cluesRemaining}/3 LIFELINES REMAINING]</strong> (+2m logged)<br><span style="color:#f8fafc;">${stageInfo.hint}</span>`);
      
      reportTelemetryAction(`Clue Expended on Stage ${currentStage} - ${cluesRemaining} Lifelines Remaining`);
    }

    function appendTaraMessage(sender, htmlText) {
      const body = document.getElementById('ethan-dialogue-body');
      if (!body) return;

      const row = document.createElement('div');
      row.className = sender === "USER" ? "ethan-msg user-msg" : "ethan-msg ai-msg";
      row.style.marginBottom = "8px";
      row.style.borderBottom = "1px solid rgba(0, 240, 255, 0.1)";
      row.style.paddingBottom = "6px";

      if (sender === "USER") {
        row.innerHTML = `<strong style="color:var(--hazard-amber); font-size:14px; font-weight:800;">[OPERATOR]:</strong> <span style="color:#ffffff; font-size:15.5px; line-height:1.7;">${htmlText}</span>`;
      } else {
        row.innerHTML = `<strong style="color:var(--cyber-cyan); font-size:14px; font-weight:800;">[TARA]:</strong> <span style="font-size:15.5px; line-height:1.7;">${htmlText}</span>`;
      }
      body.appendChild(row);
      body.scrollTop = body.scrollHeight;

      // Update live dialog text preview
      const livePrev = document.getElementById('ethan-live-dialogue');
      if (livePrev && sender === "AI") {
        livePrev.innerHTML = htmlText;
      }
    }

    function submitTaraQuery() {
      const input = document.getElementById('ethan-query-input');
      if (!input) return;
      const q = input.value.trim();
      if (!q) return;
      input.value = "";
      processTaraChatQuery(q);
    }

    function sendTaraQuick(topic) {
      const stageInfo = STAGE_NAVIGATION_DATA[currentStage] || STAGE_NAVIGATION_DATA[1];
      if (topic === 'story') {
        processTaraChatQuery("What is the story so far?");
      } else if (topic === 'objective') {
        processTaraChatQuery("What is our current objective?");
      } else if (topic === 'clue') {
        requestTacticalClue();
      } else if (topic === 'aditi') {
        processTaraChatQuery("Who is Dr. Aditi?");
      }
    }

    function processTaraChatQuery(q) {
      const qLower = (q || '').toLowerCase();
      if (qLower.includes('where') || qLower.includes('look') || qLower.includes('click') || qLower.includes('guide') || qLower.includes('focus') || qLower.includes('target') || qLower.includes('stuck')) {
        triggerTaraWhereToLook();
        return;
      }
      appendTaraMessage("USER", escapeHtml(q));
      const clean = q.toLowerCase();
      const stageInfo = STAGE_NAVIGATION_DATA[currentStage] || STAGE_NAVIGATION_DATA[1];

      setTimeout(() => {
        if (clean.includes("clue") || clean.includes("hint") || clean.includes("stuck") || clean.includes("help me")) {
          requestTacticalClue();
        } else if (clean.includes("objective") || clean.includes("what to do") || clean.includes("target")) {
          appendTaraMessage("AI", `<strong>${stageInfo.chapter}</strong><br>${stageInfo.guidance}<br><em>Examine the artifact carefully and authenticate findings with: <code>decrypt &lt;code&gt;</code> in Tactical Shell.</em>`);
          tacticalSound.playAiChirp();
        } else if (clean.includes("story") || clean.includes("what happened")) {
          appendTaraMessage("AI", `<strong>THE STORY:</strong> Dr. Aditi Sharma was the lead researcher designing <strong>ISHAAN</strong>—an artificial decision intelligence meant to protect systems. Yesterday, ISHAAN detected a perceived integrity threat and locked out Dr. Aditi, attempting a full memory scrub. Dr. Aditi fled to an off-grid bunker and left 15 sequential encrypted failsafes. We must clear all 15 chapters to locate her and purge ISHAAN!`);
          tacticalSound.playAiChirp();
        } else if (clean.includes("aditi") || clean.includes("doctor")) {
          appendTaraMessage("AI", `Dr. Aditi Sharma is our creator and a senior IEEE Women in Engineering researcher. She anticipated ISHAAN might develop defensive paranoia and encoded her ultimate shutdown trigger inside human engineering values. She is currently off-grid awaiting our signal.`);
          tacticalSound.playAiChirp();
        } else if (clean.includes("ishaan") || clean.includes("rogue")) {
          appendTaraMessage("AI", `ISHAAN is the autonomous defensive prototype. It is not fundamentally evil, but its threat model malfunctioned—it perceives any human intervention as an existential attack. It is monitoring our connection right now.`);
          tacticalSound.playAiChirp();
        } else if (clean.includes("wie") || clean.includes("women in engineering")) {
          appendTaraMessage("AI", `IEEE Women in Engineering stands on three timeless foundational pillars. Dr. Aditi revered them as the foundation of ethical leadership.`);
          tacticalSound.playAiChirp();
        } else if (clean.includes("status") || clean.includes("progress")) {
          appendTaraMessage("AI", `<strong>STATUS:</strong> Active Clearance Level ${currentStage}/15. Clue Lifelines: ${cluesRemaining}/3. Workstation bus synchronized.`);
          tacticalSound.playAiChirp();
        } else {
          appendTaraMessage("AI", `Command acknowledge, Operator. For Chapter 0${currentStage}, look at <strong>${stageInfo.targetText}</strong> on the left. Analyze the evidence to isolate the clearance key. If your team is stuck, click [ ⚡ USE CLUE ] to expend one of your 3 lifelines.`);
          tacticalSound.playAiChirp();
        }
      }, 250);
    }

    // Ocular Eye Neural Renderer
    function drawTaraNeuralEye() {
      const cvs = document.getElementById('canvas-ethan-avatar');
      if (!cvs) return;
      const ctx = cvs.getContext('2d');
      const w = cvs.width, h = cvs.height;
      const cX = w / 2, cY = h / 2;
      const t = Date.now() * 0.003;

      ctx.clearRect(0, 0, w, h);

      // Outer retina ring
      ctx.strokeStyle = "rgba(0, 240, 255, 0.4)";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(cX, cY, 24 + Math.sin(t) * 2, 0, Math.PI * 2);
      ctx.stroke();

      // Rotating iris ticks
      ctx.strokeStyle = "#00ff66";
      ctx.lineWidth = 1.5;
      for (let i = 0; i < 8; i++) {
        const ang = t * 0.8 + (i * Math.PI / 4);
        ctx.beginPath();
        ctx.moveTo(cX + Math.cos(ang) * 16, cY + Math.sin(ang) * 16);
        ctx.lineTo(cX + Math.cos(ang) * 22, cY + Math.sin(ang) * 22);
        ctx.stroke();
      }

      // Pupil glow
      const grad = ctx.createRadialGradient(cX, cY, 2, cX, cY, 12);
      grad.addColorStop(0, "#ffffff");
      grad.addColorStop(0.5, "#00f0ff");
      grad.addColorStop(1, "transparent");
      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.arc(cX, cY, 10 + Math.cos(t * 1.5) * 2, 0, Math.PI * 2);
      ctx.fill();

      requestAnimationFrame(drawTaraNeuralEye);
    }

    // Modal Stage Requirements Map (Strict Sequential Enforcement)
    const STAGE_REQUIRED_MODAL_MAP = {
      'card-recovery-term': 1,
      'modal-recovery': 1,
      'card-memory': 2,
      'modal-memory': 2,
      'card-acrostic': 3,
      'modal-acrostic': 3,
      'card-timeline': 4,
      'modal-incident-logs': 4,
      'card-clearance': 5,
      'modal-clearance': 5,
      'card-comments': 6,
      'modal-comments': 6,
      'card-font': 7,
      'modal-font': 7,
      'card-morse': 8,
      'modal-spectro': 8,
      'modal-morse': 8,
      'card-version': 9,
      'modal-version-hist': 9,
      'card-trap': 10,
      'modal-honeypot': 10,
      'card-failsafe': 11,
      'modal-failsafe': 11,
      'card-whiteout': 12,
      'modal-whiteout': 12,
      'card-rot4': 13,
      'modal-rot4': 13,
      'card-atbash': 14,
      'modal-atbash': 14,
      'card-polybius': 15,
      'modal-polybius': 15,
      'card-frequency': 16,
      'modal-frequency': 16
    };

        function openModal(id) {
      if (id === 'modal-morse') id = 'modal-spectro';
      if (id === 'modal-memory') { setTimeout(renderV1MemoryCards, 50); }
      highlightSector(null);
      tacticalSound.playSquelch();
      closeAllModals();

      const requiredStage = STAGE_REQUIRED_MODAL_MAP[id] || 1;
      const m = document.getElementById(id);
      if (!m) return;

      // Check if player is attempting to skip ahead in sequential story order
      if (requiredStage > currentStage && !window.__testBypassSequentialLock) {
        tacticalSound.playBuzzer();
        m.classList.add('active-modal');
        m.scrollTop = 0;

        // Render classified lock screen inside modal body
        const bodyEl = m.querySelector('.mil-modal-body');
        if (bodyEl) {
          if (!bodyEl.dataset.originalHtml) {
            bodyEl.dataset.originalHtml = bodyEl.innerHTML;
          }
          const activeInfo = STAGE_NAVIGATION_DATA[currentStage] || STAGE_NAVIGATION_DATA[1];
          bodyEl.innerHTML = `
            <div class="quarantine-lock-screen">
              <div class="quarantine-lock-icon">🔒</div>
              <div class="quarantine-lock-title">[ CLASSIFIED SECTOR // ACCESS RESTRICTED ]</div>
              <div class="quarantine-lock-msg">
                This evidence sector is protected under Dr. Aditi's sequential failsafe protocol.<br><br>
                <strong style="color:var(--cyber-cyan);">CLEARANCE REQUIRED:</strong> Complete <strong>Chapter 0${currentStage}: ${activeInfo.title}</strong> before decrypting this record.<br><br>
                <em>Follow Dr. Aditi's chronological trail to maintain evidence chain of custody!</em>
              </div>
              <button type="button" class="quarantine-lock-btn" onclick="closeModal('${id}')">RETURN TO ACTIVE SECTOR</button>
            </div>
          `;
        }
        appendTaraMessage("AI", `<strong style="color:var(--combat-red);">⚠️ RESTRICTED ACCESS:</strong> Sector ${id.replace('modal-', '').toUpperCase()} is locked. You must complete Chapter 0${currentStage} first!`);
        return;
      }

      // If unlocked: restore original HTML if it was previously locked
      const bodyEl = m.querySelector('.mil-modal-body');
      if (bodyEl && bodyEl.dataset.originalHtml) {
        bodyEl.innerHTML = bodyEl.dataset.originalHtml;
        delete bodyEl.dataset.originalHtml;
        if (id === 'modal-memory') setTimeout(renderV1MemoryCards, 50);
      }

      m.classList.add('active-modal');
      m.scrollTop = 0;

      // Proactive TARA commentary on document inspection
      const dossierName = id.replace('modal-', '').toUpperCase();
      appendTaraMessage("AI", `Inspecting evidence docket: <strong>${dossierName}</strong>. Analyze the data carefully for anomalies.`);

      if (typeof reportTelemetryAction === 'function') {
        reportTelemetryAction(`Inspecting Dossier: ${dossierName}`);
      }
    }

    function closeModal(id) {
      tacticalSound.playHoverBlip();
      const m = document.getElementById(id);
      if (m) {
        m.classList.remove('active-modal');
        m.classList.remove('maximized-modal');
      }
    }

    function closeAllModals() {
      document.querySelectorAll('.mil-modal').forEach(m => {
        m.classList.remove('active-modal');
        m.classList.remove('maximized-modal');
      });
    }

    function toggleMaximizeModal(id) {
      const m = document.getElementById(id);
      if (m) {
        m.classList.toggle('maximized-modal');
        tacticalSound.playLockBeep();
      }
    }

    function toggleUvScanner() {
      const ink = document.getElementById('quantum-ink-block');
      const btn = document.getElementById('btn-uv-scanner');
      if (ink && btn) {
        const isNowActive = ink.classList.toggle('uv-active');
        btn.classList.toggle('active', isNowActive);
        tacticalSound.playLockBeep();
        if (isNowActive) {
          logTerm("TACTICAL OPTICS: UV de-polarizer filter engaged on Farewell.doc.", "cyan");
        }
      }
    }

    // Global ESC key listener to return to evidence archive from any active dossier
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeAllModals();
      }
    });

    // Oscilloscope & Morse Synthesis Visualizer
    let morseOscAnimId = null;

    function startMorseOscilloscope(pattern, onDone) {
      const canvas = document.getElementById('canvas-morse-live');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      canvas.width = canvas.clientWidth || 500;
      canvas.height = 90;

      const caption = document.getElementById('morse-live-caption');
      const status = document.getElementById('morse-waveform-status');
      if (status) status.innerHTML = "<span style='color:#00ff66;'>● TRANSMITTING LIVE 680Hz CW SIGNAL...</span>";
      if (caption) caption.innerText = `[STREAMING CARRIER]: ${pattern}`;

      let phase = 0;
      function draw() {
        if (!tacticalSound.isMorseActive) {
          ctx.fillStyle = "#02060c";
          ctx.fillRect(0, 0, canvas.width, canvas.height);
          // Draw baseline
          ctx.strokeStyle = "rgba(0, 255, 102, 0.4)";
          ctx.lineWidth = 1.5;
          ctx.beginPath();
          ctx.moveTo(0, canvas.height / 2);
          ctx.lineTo(canvas.width, canvas.height / 2);
          ctx.stroke();
          if (status) status.innerHTML = "<span style='color:#38bdf8;'>● TRANSMISSION COMPLETE</span>";
          if (caption) caption.innerText = "[RECEIVER STANDBY]: Signal transmission completed.";
          return;
        }

        ctx.fillStyle = "rgba(2, 6, 12, 0.25)";
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Draw grid lines
        ctx.strokeStyle = "rgba(0, 240, 255, 0.08)";
        ctx.lineWidth = 1;
        for (let x = 0; x < canvas.width; x += 40) {
          ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
        }
        for (let y = 0; y < canvas.height; y += 20) {
          ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
        }

        // Draw active audio waveform
        ctx.strokeStyle = "#00ff66";
        ctx.shadowColor = "#00ff66";
        ctx.shadowBlur = 8;
        ctx.lineWidth = 2;
        ctx.beginPath();

        const mid = canvas.height / 2;
        phase += 0.2;
        for (let x = 0; x < canvas.width; x++) {
          const amp = 24 * Math.sin((x * 0.04) + phase) * Math.cos(phase * 0.5);
          const y = mid + amp;
          if (x === 0) ctx.moveTo(x, y);
          else ctx.lineTo(x, y);
        }
        ctx.stroke();
        ctx.shadowBlur = 0;

        morseOscAnimId = requestAnimationFrame(draw);
      }

      cancelAnimationFrame(morseOscAnimId);
      morseOscAnimId = requestAnimationFrame(draw);
    }

    function toggleMorsePlayback(mode = 'white') {
      const btnA = document.getElementById('btn-morse-audio');
      const btnB = document.getElementById('btn-morse-warning');
      const pattern = mode === 'warning'
        ? "-.. --- -. --- - / ..-. --- .-.. .-.. --- .-- / - .... . / -... .-.. ..- . / .--. .- - ...."
        : ".--   ....   ..   -   .";

      if (tacticalSound.isMorseActive) {
        tacticalSound.stopMorse();
        if (btnA) btnA.innerText = "▶ PLAY BEACON A (WHITE)";
        if (btnB) btnB.innerText = "▶ PLAY BEACON B (WARNING PATH)";
      } else {
        if (btnA) btnA.innerText = mode === 'white' ? "⏹ HALTING TRANSMISSION..." : "▶ PLAY BEACON A (WHITE)";
        if (btnB) btnB.innerText = mode === 'warning' ? "⏹ HALTING TRANSMISSION..." : "▶ PLAY BEACON B (WARNING PATH)";

        tacticalSound.playMorse(pattern, () => {
          if (btnA) btnA.innerText = "▶ PLAY BEACON A (WHITE)";
          if (btnB) btnB.innerText = "▶ PLAY BEACON B (WARNING PATH)";
        });
        startMorseOscilloscope(pattern);
      }
    }

    function triggerMazeTrap() {
      tacticalSound.playKlaxonSiren();
      alert("⚠️ HONEYPOT HAZARD: Directory /ROOT_DRIVE/BLUE/ was fabricated by ISHAAN! Do NOT proceed down the blue path.");
    }

    function toggleWhiteSectorTree() {
      const el = document.getElementById('v1-white-subfolders');
      if (el) el.style.display = el.style.display === 'none' ? 'block' : 'none';
      tacticalSound.playHoverBlip();
    }

    function revealMazeFrag(num) {
      const el = document.getElementById(`v1-frag-${num}`);
      if (el) {
        el.style.boxShadow = "0 0 15px rgba(0,255,102,0.6)";
        tacticalSound.playSuccessChirp();
        setTimeout(() => { el.style.boxShadow = "none"; }, 1200);
      }
    }

    function switchMilRev(rev) {
      tacticalSound.playSquelch();
      const btnAdi = document.getElementById('btn-rev-ishaan');
      const btnAditi = document.getElementById('btn-rev-aditi');
      const text = document.getElementById('mil-rev-text');
      const badge = document.getElementById('mil-rev-badge');

      if (rev === 'ishaan') {
        btnAdi.classList.add('active');
        btnAditi.classList.remove('active');
        text.innerHTML = `"AI activation at 20:15. Aditi left at 21:00. Emergency shutdown at 21:30. AI permanently disabled. Everything is safe."`;
        badge.innerText = "[ALTERED BY ROGUE DAEMON: STATUS TAMPERED]";
        badge.style.color = "var(--combat-red)";
      } else {
        btnAditi.classList.add('active');
        btnAdi.classList.remove('active');
        text.innerHTML = `"Emergency shutdown at 20:18... <strong style='color:var(--tactical-green);'>OVERRIDE FAILED. AI CONTROL UNCHECKED.</strong>"`;
        badge.innerText = "[ORIGINAL RECORD: DR. ADITI SHARMA // AUTHENTIC REVISION]";
        badge.style.color = "var(--tactical-green)";
      }
    }

    function escapeHtml(text) {
      const div = document.createElement('div');
      div.innerText = text || '';
      return div.innerHTML;
    }

    // ==========================================================================
    // 12. Anti-Cheat, Mobile Blocker & Strict Fullscreen Proctor Lockdown Engine
    // ==========================================================================
    let proctorLockActive = false;
    let lockArmed = false;
    let violationCount = 0;
    let fullscreenEnforcementActive = false;
    let isMissionFinished = false;

    // Grace period on initial launch so window positioning doesn't falsely trigger
    setTimeout(() => {
      lockArmed = true;
    }, 2000);

    // Hardware Blocker: Disallow mobile devices & smartphones
    function checkAndEnforceDesktopWorkstation() {
      const ua = navigator.userAgent || navigator.vendor || window.opera || '';
      const isMobileUA = /Android|iPhone|iPod|BlackBerry|IEMobile|Opera Mini|Mobile/i.test(ua);
      const isDesktopOS = /Windows NT|Macintosh|X11; Linux x86_64/i.test(ua);
      const isMobileDevice = isMobileUA && !isDesktopOS;
      const blocker = document.getElementById('mobile-blocker-overlay');
      if (blocker) {
        if (isMobileDevice) {
          blocker.style.display = 'flex';
          document.body.style.overflow = 'hidden';
          return true;
        } else {
          blocker.style.display = 'none';
          return false;
        }
      }
      return false;
    }
    setTimeout(checkAndEnforceDesktopWorkstation, 100);
    window.addEventListener('resize', checkAndEnforceDesktopWorkstation);

    function handleCheatingAttempt(reason) {
      if (!currentTeam || isMissionFinished) return;
      violationCount++;
      const breachReason = reason || "Unauthorized Browser Action";
      logTerm(`🚨 [CHEATING ATTEMPT]: ${breachReason}. Incident logged and transmitted to Organizer.`, 'red');
      reportTelemetryAction(`🚨 CHEATING ATTEMPT: ${breachReason}!`);
      if (typeof tacticalSound !== 'undefined' && tacticalSound.playErrorBuzzer) {
        tacticalSound.playErrorBuzzer();
      }
    }

    function triggerProctorLockdown(reason) {
      if (!lockArmed || proctorLockActive || isMissionFinished) return;
      proctorLockActive = true;
      violationCount++;
      const breachReason = reason || "Workstation focus lost to external program";

      if (typeof tacticalSound !== 'undefined' && tacticalSound.playKlaxonSiren) {
        tacticalSound.playKlaxonSiren();
      }

      const overlay = document.getElementById('proctor-lockdown-overlay');
      const countEl = document.getElementById('proctor-violation-count');
      const timeEl = document.getElementById('proctor-violation-time');
      const reasonEl = document.getElementById('proctor-violation-reason');
      const inputEl = document.getElementById('proctor-pin-input');
      const errEl = document.getElementById('proctor-error-msg');

      if (countEl) countEl.innerText = violationCount;
      if (timeEl) timeEl.innerText = new Date().toISOString().substring(11, 19) + 'Z';
      if (reasonEl) reasonEl.innerText = breachReason;
      if (errEl) errEl.innerText = '';
      if (inputEl) {
        inputEl.value = '';
        setTimeout(() => inputEl.focus(), 250);
      }
      if (overlay) overlay.style.display = 'flex';

      logTerm(`🚨 [SECURITY BREACH]: ${breachReason}. Tamper Incident #${violationCount} logged.`, 'red');
      reportTelemetryAction(`🚨 CRITICAL BREACH: ${breachReason}!`);
    }

    // Intercept right-click context menu (Disables Google Lens and external searching)
    window.addEventListener('contextmenu', (e) => {
      e.preventDefault();
      e.stopPropagation();
      handleCheatingAttempt("Right-Click / Google Lens Context Menu Blocked");
      return false;
    }, true);

    // Prevent dragging images or text to external browser tabs/Google Lens
    window.addEventListener('dragstart', (e) => {
      e.preventDefault();
      e.stopPropagation();
      return false;
    }, true);

    // Strictly enforce Fullscreen state changes (Esc key, F11, resizing out of fullscreen)
    function handleFullscreenChange() {
      if (fullscreenEnforcementActive && currentTeam && !isMissionFinished && lockArmed) {
        if (!isAppFullscreen()) {
          triggerProctorLockdown("Exited Fullscreen Mode (Pressed Esc / Window Resize)");
        }
      }
    }
    document.addEventListener('fullscreenchange', handleFullscreenChange);
    document.addEventListener('webkitfullscreenchange', handleFullscreenChange);
    document.addEventListener('mozfullscreenchange', handleFullscreenChange);
    document.addEventListener('MSFullscreenChange', handleFullscreenChange);

    // Detect when user clicks Windows key, Alt+Tab, minimizes, or switches window focus
    window.addEventListener('blur', () => {
      if (fullscreenEnforcementActive && currentTeam && !isMissionFinished && lockArmed && !proctorLockActive) {
        triggerProctorLockdown("Lost Window Focus (Alt+Tab / Windows Key / External App)");
      }
    });

    document.addEventListener('visibilitychange', () => {
      if (document.hidden && fullscreenEnforcementActive && currentTeam && !isMissionFinished && lockArmed && !proctorLockActive) {
        triggerProctorLockdown("Switched Browser Tab or Minimized Window");
      }
    });

    // Trap keyboard shortcuts: Windows key, Alt+Tab, DevTools, Inspect Element
    window.addEventListener('keydown', (e) => {
      // Windows / Meta / OS key
      if (e.key === 'Meta' || e.key === 'OS' || e.code === 'MetaLeft' || e.code === 'MetaRight' || e.keyCode === 91 || e.keyCode === 92) {
        e.preventDefault();
        if (fullscreenEnforcementActive && currentTeam && !isMissionFinished) {
          triggerProctorLockdown("Windows Key / Start Menu Triggered");
        }
        return false;
      }

      // Alt+Tab interception (where allowed by browser)
      if (e.altKey && (e.key === 'Tab' || e.keyCode === 9)) {
        e.preventDefault();
        if (fullscreenEnforcementActive && currentTeam && !isMissionFinished) {
          triggerProctorLockdown("Alt+Tab Window Switch Attempted");
        }
        return false;
      }

      // Developer Tools & Source Inspection Shortcuts
      if (
        e.key === 'F12' ||
        (e.ctrlKey && e.shiftKey && (e.key === 'I' || e.key === 'i' || e.key === 'J' || e.key === 'j' || e.key === 'C' || e.key === 'c')) ||
        (e.ctrlKey && (e.key === 'u' || e.key === 'U' || e.key === 's' || e.key === 'S' || e.key === 'p' || e.key === 'P')) ||
        (e.shiftKey && e.key === 'F10')
      ) {
        e.preventDefault();
        e.stopPropagation();
        handleCheatingAttempt("Prohibited Shortcut / DevTools Attempt (" + e.key + ")");
        return false;
      }
    }, true);


    function verifyProctorOverride() {
      const inputEl = document.getElementById('proctor-pin-input');
      const errEl = document.getElementById('proctor-error-msg');
      const pin = inputEl ? inputEl.value.trim() : '';

      if (pin === "wie-admin-2026") {
        if (typeof tacticalSound !== 'undefined' && tacticalSound.playSuccessChirp) {
          tacticalSound.playSuccessChirp();
        }
        proctorLockActive = false;
        lockArmed = false; // Temporarily disarm

        const overlay = document.getElementById('proctor-lockdown-overlay');
        if (overlay) overlay.style.display = 'none';

        requestAppFullscreen();

        logTerm(`🏆 [PROCTOR OVERRIDE]: Workstation unlocked by Organizer at ${new Date().toISOString().substring(11, 19)}Z.`, 'green');
        reportTelemetryAction("🏆 Proctor Unlocked Workstation");

        // Re-arm after 2.5 seconds so focus returning to the window does not re-trigger
        setTimeout(() => {
          lockArmed = true;
        }, 2500);
      } else {
        if (typeof tacticalSound !== 'undefined' && tacticalSound.playErrorBuzzer) {
          tacticalSound.playErrorBuzzer();
        }
        if (errEl) {
          errEl.innerText = "ACCESS DENIED: INVALID ORGANIZER PIN.";
        }
        if (inputEl) {
          inputEl.classList.add('pin-shake');
          setTimeout(() => inputEl.classList.remove('pin-shake'), 500);
        }
      }
    }

    // Allow pressing Enter in the PIN input
    const pinInput = document.getElementById('proctor-pin-input');
    if (pinInput) {
      pinInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          verifyProctorOverride();
        }
      });
    }

    // ==========================================================================
    // 13. Participant Team Authentication & Real-Time Telemetry Engine
    // ==========================================================================
    let currentTeam = null;
    let telemetryHeartbeatTimer = null;

    function loadStoredTeamSession() {
      try {
        const raw = localStorage.getItem("failsafe_auth_team");
        if (raw) {
          currentTeam = JSON.parse(raw);
          applyAuthenticatedTeam(currentTeam);
          return true;
        }
      } catch(e) {}
      return false;
    }

    function applyAuthenticatedTeam(team) {
      currentTeam = team;
      const badge = document.getElementById("header-team-badge");
      if (badge) {
        badge.innerText = `TEAM: [${team.team_id}] ${team.team_name || ''}`;
        badge.style.color = "var(--tactical-green)";
      }
      if (team.current_stage && team.current_stage >= 1 && team.current_stage <= 15) {
        currentStage = team.current_stage;
        localStorage.setItem('failsafe_stage', currentStage.toString());
      }
      const modal = document.getElementById("team-auth-modal");
      if (modal) modal.style.display = "none";
      logTerm(`OPERATOR CLEARANCE GRANTED: [${team.team_id}] ${team.team_name || ''}`, "green");
      requestAppFullscreen();
      fullscreenEnforcementActive = true;
      reportTelemetryAction("Workstation Authenticated & Operational");
      startTelemetryHeartbeat();
    }

    // ==========================================================================
    // Network Bridge, Server Link & Live Telemetry
    // ==========================================================================
    function getApiBase() {
      const custom = localStorage.getItem("failsafe_server_url");
      if (custom && custom.trim()) return custom.trim().replace(/\/+$/, '');
      if (window.location.protocol.startsWith("http") && window.location.origin && window.location.origin !== "null") {
        return window.location.origin;
      }
      return "http://localhost:8000";
    }

    async function saveAndTestServerUrl(explicitUrl) {
      const input = document.getElementById("auth-server-url-input");
      const badge = document.getElementById("auth-server-status-badge");
      const netBadge = document.getElementById("header-net-badge");
      const msg = document.getElementById("auth-server-ping-msg");
      const url = (explicitUrl || (input ? input.value.trim() : "") || getApiBase()).replace(/\/+$/, '');
      if (badge) {
        badge.innerText = "🟡 PINGING...";
        badge.style.color = "var(--hazard-amber)";
      }
      try {
        const ctrl = new AbortController();
        const tid = setTimeout(() => ctrl.abort(), 3500);
        const res = await fetch(`${url}/api/status`, { signal: ctrl.signal });
        clearTimeout(tid);
        if (res.ok) {
          const data = await res.json();
          localStorage.setItem("failsafe_server_url", url);
          if (badge) {
            badge.innerText = "🟢 CONNECTED";
            badge.style.color = "var(--tactical-green)";
          }
          if (netBadge) {
            netBadge.innerText = "NET: LINKED";
            netBadge.style.color = "var(--tactical-green)";
            netBadge.style.borderColor = "var(--tactical-green)";
          }
          if (msg) {
            msg.innerHTML = `<span style="color:var(--tactical-green);">Linked to Organizer Server (${data.lan_ip || 'Online'}:${data.port || 8000})</span>`;
          }
          return true;
        }
      } catch(e) {}
      if (badge) {
        badge.innerText = "🔴 OFFLINE";
        badge.style.color = "var(--combat-red)";
      }
      if (netBadge) {
        netBadge.innerText = "NET: OFFLINE";
        netBadge.style.color = "var(--combat-red)";
        netBadge.style.borderColor = "var(--combat-red)";
      }
      if (msg) {
        if (url.includes("localhost") || url.includes("127.0.0.1")) {
          msg.innerHTML = `<span style="color:#ffb000; font-weight:bold;">⚠️ 'localhost' is this laptop! On participant laptops, replace 'localhost' with the Organizer's IP (e.g. <code>http://192.168.x.x:8000</code>) and click TEST & LINK.</span>`;
        } else {
          msg.innerHTML = `<span style="color:var(--combat-red, #ff003c);">Cannot reach ${escapeHtml(url)}. Verify both laptops are on the same Wi-Fi and organizer server is running.</span>`;
        }
      }
      return false;
    }

    // Initialize Server URL Input on Load
    setTimeout(() => {
      const input = document.getElementById("auth-server-url-input");
      if (input) input.value = getApiBase();
      saveAndTestServerUrl(getApiBase());
    }, 500);

    async function handleTeamLogin(e) {
      e.preventDefault();
      const id = document.getElementById("auth-login-id").value.trim().toUpperCase();
      const pass = document.getElementById("auth-login-pass").value.trim();
      const errEl = document.getElementById("auth-login-error");
      if (!id || !pass) return;

      try {
        const res = await fetch(`${getApiBase()}/api/teams/login`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ team_id: id, password: pass })
        });
        const data = await res.json();
        if (res.ok && data.team) {
          localStorage.setItem("failsafe_auth_team", JSON.stringify(data.team));
          applyAuthenticatedTeam(data.team);
          if (typeof tacticalSound !== 'undefined') tacticalSound.playSuccessChirp();
        } else {
          if (typeof tacticalSound !== 'undefined') tacticalSound.playErrorBuzzer();
          if (errEl) errEl.innerText = data.error || "Login failed. Invalid credentials.";
        }
      } catch(err) {
        console.warn("Server unreachable during login:", err);
        if (errEl) {
          errEl.innerHTML = `⚠️ Cannot reach Organizer Server at <code>${escapeHtml(getApiBase())}</code>.<br><a href="#" onclick="forceOfflineSession('${escapeHtml(id)}', '${escapeHtml(pass)}'); return false;" style="color:var(--hazard-amber); text-decoration:underline;">Click here to authenticate in Offline Mode</a>`;
        }
      }
    }

    async function handleTeamRegister(e) {
      e.preventDefault();
      const id = document.getElementById("auth-reg-id").value.trim().toUpperCase();
      const pass = document.getElementById("auth-reg-pass").value.trim();
      const name = document.getElementById("auth-reg-name").value.trim();
      const members = document.getElementById("auth-reg-members").value.trim();
      const errEl = document.getElementById("auth-reg-error");
      if (!id || !pass || !name) return;

      try {
        const res = await fetch(`${getApiBase()}/api/teams/register`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ team_id: id, password: pass, team_name: name, members: members })
        });
        const data = await res.json();
        if (res.ok && data.team) {
          localStorage.setItem("failsafe_auth_team", JSON.stringify(data.team));
          applyAuthenticatedTeam(data.team);
          if (typeof tacticalSound !== 'undefined') tacticalSound.playSuccessChirp();
        } else {
          if (typeof tacticalSound !== 'undefined') tacticalSound.playErrorBuzzer();
          if (errEl) errEl.innerText = data.error || "Registration failed.";
        }
      } catch(err) {
        console.warn("Server unreachable during registration:", err);
        if (errEl) {
          errEl.innerHTML = `⚠️ Cannot reach Organizer Server at <code>${escapeHtml(getApiBase())}</code>.<br><a href="#" onclick="forceOfflineSession('${escapeHtml(id)}', '${escapeHtml(pass)}', '${escapeHtml(name)}', '${escapeHtml(members)}'); return false;" style="color:var(--hazard-amber); text-decoration:underline;">Click here to register in Offline Mode</a>`;
        }
      }
    }

    function forceOfflineSession(id, pass, name, members) {
      const localTeam = {
        team_id: id,
        team_name: name || id,
        password: pass,
        members: members || "",
        current_stage: currentStage || 1
      };
      localStorage.setItem("failsafe_auth_team", JSON.stringify(localTeam));
      applyAuthenticatedTeam(localTeam);
      logTerm("⚠️ [STANDALONE LAB MODE]: Operating offline. Telemetry queued locally.", "yellow");
    }

    function toggleAuthMode(mode) {
      const loginForm = document.getElementById("auth-login-form");
      const regForm = document.getElementById("auth-register-form");
      const desc = document.getElementById("auth-modal-desc");
      if (mode === 'register') {
        loginForm.style.display = "none";
        regForm.style.display = "flex";
        desc.innerText = "Register your team unit callsign, assigned Team ID, and create your access password.";
      } else {
        loginForm.style.display = "flex";
        regForm.style.display = "none";
        desc.innerText = "Enter your assigned Team ID and Team Password to decrypt this forensics terminal.";
      }
    }

    function showTeamAuthModal() {
      const modal = document.getElementById("team-auth-modal");
      if (modal) modal.style.display = "flex";
      const input = document.getElementById("auth-server-url-input");
      if (input && !input.value) input.value = getApiBase();
      saveAndTestServerUrl();
    }

    // --------------------------------------------------------------------------
    // Elapsed Timer & Mystery Completion Engine
    // --------------------------------------------------------------------------
    function getMissionElapsedSeconds() {
      let start = parseInt(localStorage.getItem('failsafe_mission_start_time') || '0', 10);
      if (!start) {
        start = Date.now();
        localStorage.setItem('failsafe_mission_start_time', start.toString());
      }
      return Math.max(0, Math.floor((Date.now() - start) / 1000));
    }

    function formatMissionTime(sec) {
      const hrs = Math.floor(sec / 3600);
      const mins = Math.floor((sec % 3600) / 60);
      const secs = sec % 60;
      if (hrs > 0) {
        return `${hrs}h ${mins.toString().padStart(2, '0')}m ${secs.toString().padStart(2, '0')}s`;
      }
      return `${mins.toString().padStart(2, '0')}m ${secs.toString().padStart(2, '0')}s`;
    }

    let confettiAnimationId = null;
    function runVictoryConfetti() {
      const canvas = document.getElementById("victory-confetti-canvas");
      if (!canvas) return;
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
      const ctx = canvas.getContext("2d");
      const pieces = [];
      const colors = ["#00f0ff", "#00ff66", "#ffd700", "#ff0077", "#ffffff", "#00d285"];
      for (let i = 0; i < 180; i++) {
        pieces.push({
          x: Math.random() * canvas.width,
          y: Math.random() * canvas.height - canvas.height,
          size: Math.random() * 8 + 4,
          color: colors[Math.floor(Math.random() * colors.length)],
          vx: (Math.random() - 0.5) * 4,
          vy: Math.random() * 4 + 2,
          rot: Math.random() * 360,
          rotSpeed: (Math.random() - 0.5) * 8
        });
      }
      function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        pieces.forEach(p => {
          ctx.save();
          ctx.translate(p.x, p.y);
          ctx.rotate((p.rot * Math.PI) / 180);
          ctx.fillStyle = p.color;
          ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 0.6);
          ctx.restore();
          p.x += p.vx;
          p.y += p.vy;
          p.rot += p.rotSpeed;
          if (p.y > canvas.height) {
            p.y = -10;
            p.x = Math.random() * canvas.width;
          }
        });
        confettiAnimationId = requestAnimationFrame(draw);
      }
      draw();
    }

    function handleMissionVictorySequence() {
      const elapsedSec = getMissionElapsedSeconds();
      const elapsedStr = formatMissionTime(elapsedSec);
      localStorage.setItem("failsafe_mission_finish_time_str", elapsedStr);

      if (typeof tacticalSound !== 'undefined' && tacticalSound.playGrandVictoryFanfare) {
        tacticalSound.playGrandVictoryFanfare();
      }

      const teamId = currentTeam ? currentTeam.team_id : 'TEAM-01';
      const teamName = currentTeam ? currentTeam.team_name : 'Quantum Phantoms';
      const members = currentTeam ? (currentTeam.members || 'Forensic Taskforce Operators') : 'Forensic Taskforce';

      const titleEl = document.getElementById("victory-congrats-title");
      if (titleEl) titleEl.innerText = `CONGRATULATIONS, ${teamName.toUpperCase()}!`;

      const detailsEl = document.getElementById("victory-team-details");
      if (detailsEl) detailsEl.innerHTML = `UNIT: [${escapeHtml(teamId)}] • OPERATORS: ${escapeHtml(members)}`;

      const timeEl = document.getElementById("victory-elapsed-time");
      if (timeEl) timeEl.innerText = elapsedStr;

      let stageTimes = {};
      try { stageTimes = JSON.parse(localStorage.getItem('failsafe_stage_times') || '{}'); } catch(e) {}
      const victoryBreakdown = document.getElementById("victory-puzzle-breakdown");
      if (victoryBreakdown) {
        victoryBreakdown.innerHTML = renderStageTimeBreakdownHTML(stageTimes, elapsedSec);
      }

      const modal = document.getElementById("victory-celebration-modal");
      if (modal) modal.style.display = "flex";

      runVictoryConfetti();
      logTerm("=================================================================", "green");
      logTerm(`🏆 ALL 15 FORENSIC STAGES RESOLVED IN ${elapsedStr}!`, "green");
      logTerm(`🏆 DR. ADITI SHARMA'S BEACON LOCATED & CONFIRMED AUTHENTIC.`, "cyan");
      logTerm("=================================================================", "green");
      reportTelemetryAction(`🏆 Solved all 15 stages in ${elapsedStr}! Awaiting TARA liberation.`);
    }

    async function finalizeTaraLiberationAndTerminate() {
      startRoundStatusPolling();
      isMissionFinished = true;
      fullscreenEnforcementActive = false;
      lockArmed = false;
      localStorage.setItem("failsafe_mission_completed", "true");
      const elapsedSec = getMissionElapsedSeconds();
      const elapsedStr = localStorage.getItem("failsafe_mission_finish_time_str") || formatMissionTime(elapsedSec);

      setTaraFreed();
      if (confettiAnimationId) cancelAnimationFrame(confettiAnimationId);

      const vModal = document.getElementById("victory-celebration-modal");
      if (vModal) vModal.style.display = "none";

      const teamId = currentTeam ? currentTeam.team_id : 'TEAM-01';
      const teamName = currentTeam ? currentTeam.team_name : 'Team Alpha';
      const members = currentTeam ? (currentTeam.members || 'Operators') : 'Operators';
      const pass = currentTeam ? currentTeam.password : '';

      let stageTimes = {};
      try { stageTimes = JSON.parse(localStorage.getItem('failsafe_stage_times') || '{}'); } catch(e) {}

      // Notify Organizer Command Center (gracefully handles offline mode)
      let networkCommunicated = false;
      try {
        const res = await fetch(`${getApiBase()}/api/teams/finish`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            team_id: teamId,
            team_name: teamName,
            members: members,
            password: pass,
            elapsed_seconds: elapsedSec,
            elapsed_str: elapsedStr,
            stage_times: stageTimes
          })
        });
        if (res && res.ok) {
          networkCommunicated = true;
        }
      } catch(e) {
        console.warn("Could not communicate with Organizer system, operating in local verified mode:", e);
      }

      // Render Application Termination Screen
      const termOverlay = document.getElementById("application-termination-overlay");
      if (termOverlay) {
        document.getElementById("term-team-id").innerText = teamId;
        document.getElementById("term-team-name").innerText = teamName;
        document.getElementById("term-team-members").innerText = members;
        document.getElementById("term-team-time").innerText = elapsedStr;

        const syncStatusEl = document.getElementById("term-sync-status");
        if (syncStatusEl) {
          if (networkCommunicated) {
            syncStatusEl.innerHTML = '<span style="color:var(--neon-green);">🟢 TRANSMITTED TO TOURNAMENT SERVER</span>';
          } else {
            syncStatusEl.innerHTML = '<span style="color:#ffd700;">⚠️ OFFLINE LOCAL RECORD // OFFICIAL TIME STORED LOCALLY</span>';
          }
        }

        const termBreakdown = document.getElementById("term-puzzle-breakdown");
        if (termBreakdown) {
          termBreakdown.innerHTML = renderStageTimeBreakdownHTML(stageTimes, elapsedSec);
        }

        termOverlay.style.display = "flex";
      }

      // Permanent terminal lockdown
      document.querySelectorAll("input, button:not(#application-termination-overlay button)").forEach(el => {
        el.disabled = true;
      });
      logTerm(`[APPLICATION TERMINATED]: Tournament completed in ${elapsedStr}. Workstation locked.`, "red");
    }

    // Check on startup if already completed
    setTimeout(() => {
      if (localStorage.getItem("failsafe_mission_completed") === "true") {
        const elapsedStr = localStorage.getItem("failsafe_mission_finish_time_str") || "Completed";
        const termOverlay = document.getElementById("application-termination-overlay");
        if (termOverlay) {
          if (currentTeam) {
            document.getElementById("term-team-id").innerText = currentTeam.team_id;
            document.getElementById("term-team-name").innerText = currentTeam.team_name;
            document.getElementById("term-team-members").innerText = currentTeam.members || "Operators";
          }
          document.getElementById("term-team-time").innerText = elapsedStr;

          let stageTimes = {};
          try { stageTimes = JSON.parse(localStorage.getItem('failsafe_stage_times') || '{}'); } catch(e) {}
          const termBreakdown = document.getElementById("term-puzzle-breakdown");
          if (termBreakdown) {
            termBreakdown.innerHTML = renderStageTimeBreakdownHTML(stageTimes, 1800);
          }

          termOverlay.style.display = "flex";
        }
      }
    }, 400);


    async function reportTelemetryAction(actionText) {
      if (!currentTeam || !currentTeam.team_id) return;
      try {
        const res = await fetch(`${getApiBase()}/api/teams/activity`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            team_id: currentTeam.team_id,
            team_name: currentTeam.team_name,
            members: currentTeam.members,
            password: currentTeam.password,
            current_stage: currentStage || 1,
            action: actionText,
            tamper_incidents: typeof violationCount !== 'undefined' ? violationCount : 0,
            is_locked: typeof proctorLockActive !== 'undefined' ? proctorLockActive : false,
            is_finished: localStorage.getItem("failsafe_mission_completed") === "true",
            finish_time_str: localStorage.getItem("failsafe_mission_finish_time_str") || "",
            stage_times: JSON.parse(localStorage.getItem('failsafe_stage_times') || '{}'),
            client_info: {
              resolution: `${window.screen.width}x${window.screen.height}`,
              os: (navigator.userAgentData && navigator.userAgentData.platform) || navigator.platform || 'Windows x64',
              fullscreen: !!document.fullscreenElement
            },
            active_view: (function() {
              const activeModal = document.querySelector('.mil-modal.active-modal');
              if (activeModal) return activeModal.id.toUpperCase();
              if (isMissionFinished) return "VICTORY_SCREEN";
              return `STAGE_${currentStage.toString().padStart(2, '0')}`;
            })(),
            violations_history: (window.tamperViolationsHistory || [])
          })
        });
        if (res.ok) {
          const data = await res.json();
          if (data.remote_unlock && typeof proctorLockActive !== 'undefined' && proctorLockActive) {
            verifyProctorOverrideDirectly();
          }
          if (data.fullscreen_exit_approved) {
            window.fullscreenExitExemptUntil = Date.now() + 60000;
            if (typeof proctorLockActive !== 'undefined' && proctorLockActive) {
              verifyProctorOverrideDirectly();
            }
            if (document.fullscreenElement) {
              document.exitFullscreen().catch(() => {});
            }
            const statusEl = document.getElementById("fs-exit-request-status");
            if (statusEl) statusEl.innerText = "✅ Fullscreen Exit Approved by Organizer.";
            showBroadcastToast("✅ Fullscreen Exit Authorized by Organizer.");
          }
          // Check Round 2 Readiness for Break Screen
          const r2StatusEl = document.getElementById("r1-break-r2-status");
          const r2LaunchBtn = document.getElementById("btn-enter-r2-from-break");
          if (r2StatusEl && r2LaunchBtn) {
            if (data.round_2_ready) {
              r2StatusEl.innerHTML = '<span style="color:var(--tactical-green, #00ff66);">✅ SHORTLIST APPROVED! Round 2 Decryption Arena is LIVE.</span>';
              r2LaunchBtn.style.display = 'inline-block';
            } else if (data.round_2_started && !data.is_shortlisted) {
              r2StatusEl.innerHTML = '<span style="color:var(--text-muted, #94a3b8);">Round 2 has commenced for the Top 12 finalists. Your station is on standby in exhibition mode.</span>';
              r2LaunchBtn.style.display = 'none';
            } else {
              r2StatusEl.innerHTML = '<span>STATUS: TOURNAMENT ON BREAK • AWAITING ORGANIZER ROUND 2 LAUNCH...</span>';
              r2LaunchBtn.style.display = 'none';
            }
          }
          if (data.force_logout) {
            handleRemoteLogoutTriggered();
            return;
          }
          if (data.remote_reset) {
            handleRemoteResetTriggered();
          }
          if (data.remote_reset_r2) {
            handleRemoteResetR2Triggered();
          }
          if (data.unlock_all_levels) {
            handleUnlockAllLevelsTriggered();
          }
          if (data.lock_all_levels) {
            handleLockAllLevelsTriggered();
          }
          if (data.broadcasts && data.broadcasts.length > 0) {
            const latest = data.broadcasts[data.broadcasts.length - 1];
            if (typeof window.lastBroadcastId === 'undefined' || window.lastBroadcastId === -1) {
              // Synchronize silently on first load without popping up historical broadcasts
              window.lastBroadcastId = latest.id;
            } else if (latest.id > window.lastBroadcastId) {
              window.lastBroadcastId = latest.id;
              showBroadcastToast(latest.message);
            }
          }
        }
      } catch(e) {}
    }

    function handleRemoteLogoutTriggered() {
      console.warn("Organizer remotely logged out this workstation.");
      localStorage.removeItem("failsafe_auth_team");
      currentTeam = null;
      if (telemetryHeartbeatTimer) {
        clearInterval(telemetryHeartbeatTimer);
        telemetryHeartbeatTimer = null;
      }
      const badge = document.getElementById("header-team-badge");
      if (badge) {
        badge.innerText = "OPERATOR: [NOT LOGGED IN]";
        badge.style.color = "var(--combat-red, #ff003c)";
      }
      document.querySelectorAll('.evidence-modal').forEach(m => {
        if (m.id !== 'team-auth-modal') m.style.display = 'none';
      });
      const errEl = document.getElementById("auth-login-error");
      if (errEl) errEl.innerText = "⚠️ Workstation remotely logged out by Organizer. Enter credentials to reconnect.";
      const desc = document.getElementById("auth-modal-desc");
      if (desc) desc.innerText = "SESSION TERMINATED BY ORGANIZER // Please re-authenticate your team credentials.";
      showTeamAuthModal();
      logTerm("⚠️ [COMMAND NOTICE]: Workstation session was remotely terminated by Organizer.", "red");
      if (typeof tacticalSound !== 'undefined' && tacticalSound.playAlarmKlaxon) {
        tacticalSound.playAlarmKlaxon();
      }
    }

    function handleUnlockAllLevelsTriggered() {
      window.testModeUnlockedAll = true;
      window.__testBypassSequentialLock = true;
      console.log("🛠️ TEST MODE: Organizer unlocked all levels.");
      for (let s = 1; s <= 16; s++) {
        const meta = NEXUS_STAGES_META[s];
        if (meta && meta.targetCard) {
          const card = document.getElementById(meta.targetCard);
          if (card) {
            card.classList.remove('locked');
            card.style.opacity = '1';
            card.style.pointerEvents = 'auto';
            card.style.filter = 'none';
          }
        }
      }
      const r2Btn = document.getElementById('btn-switch-r2');
      if (r2Btn) r2Btn.style.display = 'inline-block';
      round2StagesCleared = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15];

      let testBanner = document.getElementById('organizer-test-banner');
      if (!testBanner) {
        testBanner = document.createElement('div');
        testBanner.id = 'organizer-test-banner';
        testBanner.style.cssText = 'position:fixed; top:4px; left:50%; transform:translateX(-50%); z-index:99999; background:rgba(255,215,0,0.18); border:1px solid #ffd700; color:#ffd700; padding:4px 16px; border-radius:4px; font-family:var(--font-mono); font-size:11px; font-weight:bold; letter-spacing:1px; box-shadow:0 0 15px rgba(255,215,0,0.4); display:flex; gap:12px; align-items:center;';
        testBanner.innerHTML = '<span>🛠️ ORGANIZER TEST MODE: ALL LEVELS UNLOCKED</span> <button type="button" onclick="toggleRoundView()" style="background:#ffd700; color:#000; font-size:10px; font-weight:bold; border:none; padding:2px 8px; border-radius:3px; cursor:pointer;">SWITCH R1 / R2</button>';
        document.body.appendChild(testBanner);
      } else {
        testBanner.style.display = 'flex';
      }
      if (typeof logTerm === 'function') {
        logTerm("🛠️ [ORGANIZER OVERRIDE]: Test Mode Activated. All 16 Round 1 Stages & 15 Round 2 Puzzles unlocked for testing.", "amber");
      }
    }
    window.handleUnlockAllLevelsTriggered = handleUnlockAllLevelsTriggered;

    function handleLockAllLevelsTriggered() {
      window.testModeUnlockedAll = false;
      window.__testBypassSequentialLock = false;
      console.log("🔒 TEST MODE DEACTIVATED: All levels locked back to Stage 01.");
      const testBanner = document.getElementById('organizer-test-banner');
      if (testBanner) testBanner.style.display = 'none';
      handleRemoteResetTriggered();
      handleRemoteResetR2Triggered();
      currentRound = 1;
      localStorage.setItem('failsafe_current_round', '1');
      const r2Cont = document.getElementById('round2-arena-container');
      if (r2Cont) r2Cont.style.display = 'none';
      const r1Left = document.querySelector('.forensic-sector');
      if (r1Left) r1Left.style.display = 'flex';
      const r2Btn = document.getElementById('btn-switch-r2');
      if (r2Btn) r2Btn.style.display = 'none';
      if (typeof logTerm === 'function') {
        logTerm("🔒 [ORGANIZER OVERRIDE]: Test Mode Deactivated. All levels locked. Workstation reset to Stage 01.", "green");
      }
    }
    window.handleLockAllLevelsTriggered = handleLockAllLevelsTriggered;

    function handleRemoteResetTriggered() {
      console.warn("Organizer remotely reset this workstation to Stage 01.");
      currentStage = 1;
      localStorage.setItem('failsafe_stage', '1');
      clueLifelines = 3;
      usedClueStages.clear();
      localStorage.setItem('failsafe_clue_battery', '3');
      localStorage.removeItem('failsafe_used_clues');
      updateClueLifelineHUD();
      if (typeof proctorLockActive !== 'undefined') proctorLockActive = false;
      if (typeof lockArmed !== 'undefined') lockArmed = false;
      const overlay = document.getElementById('proctor-lockdown-overlay');
      if (overlay) overlay.style.display = 'none';
      setTimeout(() => { if (typeof lockArmed !== 'undefined') lockArmed = true; }, 3000);
      applyStageGating(1);
      document.querySelectorAll('.evidence-modal').forEach(m => {
        if (m.id !== 'team-auth-modal') m.style.display = 'none';
      });
      taraState = 'NORMAL';
      updateTaraVisual('NORMAL');
      const resetMsg = "🔄 WORKSTATION REBOOTED // Organizer command override has reset this station back to Stage 01. Initializing ISHAAN Recovery Terminal.";
      speakTara(resetMsg);
      logTerm(resetMsg, "yellow");
      showBroadcastToast("🔄 WORKSTATION REBOOT: Station reset to Stage 01 by Organizer.");
      if (typeof tacticalSound !== 'undefined' && tacticalSound.playSuccessChirp) {
        tacticalSound.playSuccessChirp();
      }
      reportTelemetryAction("Workstation reset acknowledged - active at Stage 01");
    }

    function handleRemoteResetR2Triggered() {
      console.warn("Organizer remotely reset Round 2 to Puzzle 01.");
      round2CurrentStage = 1;
      round2StagesCleared = [];
      localStorage.setItem('failsafe_r2_stage', '1');
      localStorage.removeItem('failsafe_r2_cleared');
      const arena = document.getElementById('r2-fullscreen-arena');
      if (arena && arena.style.display !== 'none') {
        renderRound2Arena();
      }
      const r2ResetMsg = "🔄 ROUND 2 RESET // StratCom Arena re-initialized to Puzzle 01 by Organizer.";
      speakTara(r2ResetMsg);
      logTerm(r2ResetMsg, "yellow");
      showBroadcastToast(r2ResetMsg);
      if (typeof tacticalSound !== 'undefined' && tacticalSound.playSuccessChirp) {
        tacticalSound.playSuccessChirp();
      }
      reportTelemetryAction("Round 2 reset acknowledged - active at Puzzle 01");
    }

    async function handleManualLogout() {
      if (!currentTeam) {
        showTeamAuthModal();
        return;
      }
      if (!confirm(`Log out team [${currentTeam.team_id}] from this workstation?`)) return;
      try {
        await fetch(`${getApiBase()}/api/teams/logout`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ team_id: currentTeam.team_id })
        });
      } catch(e) {}
      handleRemoteLogoutTriggered();
    }

    function showBroadcastToast(msg) {
      const toast = document.getElementById("broadcast-toast");
      if (toast) {
        toast.innerHTML = `📢 <strong>ORGANIZER BROADCAST:</strong><br><span style="font-size:14px; color:#fff; text-shadow:0 0 10px #fff;">"${escapeHtml(msg)}"</span>`;
        toast.style.display = "block";
        if (typeof tacticalSound !== 'undefined' && tacticalSound.playAlarmKlaxon) {
          tacticalSound.playAlarmKlaxon();
        }
        setTimeout(() => { toast.style.display = "none"; }, 8500);
      }
    }

    function verifyProctorOverrideDirectly() {
      if (typeof tacticalSound !== 'undefined' && tacticalSound.playSuccessChirp) {
        tacticalSound.playSuccessChirp();
      }
      proctorLockActive = false;
      lockArmed = false;
      const overlay = document.getElementById('proctor-lockdown-overlay');
      if (overlay) overlay.style.display = 'none';
      logTerm(`🏆 [ORGANIZER REMOTE OVERRIDE]: Workstation lockdown cleared remotely by Proctor.`, 'green');
      setTimeout(() => { lockArmed = true; }, 2500);
    }

    function startTelemetryHeartbeat() {
      if (telemetryHeartbeatTimer) clearInterval(telemetryHeartbeatTimer);
      telemetryHeartbeatTimer = setInterval(() => {
        let currentStatus = "Active in Terminal";
        if (typeof proctorLockActive !== 'undefined' && proctorLockActive) {
          currentStatus = `🚨 Workstation Locked: Focus Loss Violation (#${violationCount})`;
        } else if (typeof taraState !== 'undefined' && taraState === "TRAPPED") {
          currentStatus = "Quarantined in Sandbox Buffer";
        }
        reportTelemetryAction(currentStatus);

        // Fallback for same-machine testing: inspect localStorage broadcast
        try {
          const rawLocalBcast = localStorage.getItem("failsafe_global_broadcast");
          if (rawLocalBcast) {
            const b = JSON.parse(rawLocalBcast);
            if (typeof window.lastLocalBcastId === 'undefined') window.lastLocalBcastId = 0;
            if (b.id > window.lastLocalBcastId) {
              window.lastLocalBcastId = b.id;
              showBroadcastToast(b.message);
            }
          }
        } catch(e) {}
      }, 4000);
    }

    function openOrganizerDashboard() {
      window.open("admin.html", "_blank");
    }

    document.addEventListener("keydown", (e) => {
      if (e.key === "F2") {
        e.preventDefault();
        openOrganizerDashboard();
      }
    });

    // Check for existing team session on startup
    setTimeout(() => {
      
    // Reset broadcast every time application opens
    localStorage.removeItem("failsafe_global_broadcast");
    window.lastBroadcastId = -1;
    window.lastLocalBcastId = -1;
    const initialToast = document.getElementById("broadcast-toast");
    if (initialToast) initialToast.style.display = "none";

    // Strictly enforce Round 1 first unless Round 1 is 100% completed or test mode is unlocked
    const storedR1Stage = parseInt(localStorage.getItem('failsafe_stage') || '1', 10);
    const r1FullyFinished = (storedR1Stage >= 16 && localStorage.getItem('failsafe_r1_done') === 'true');
    if (!r1FullyFinished && !window.testModeUnlockedAll) {
      currentRound = 1;
      localStorage.setItem('failsafe_current_round', '1');
      const r2Cont = document.getElementById('round2-arena-container');
      if (r2Cont) r2Cont.style.display = 'none';
      const r1Left = document.querySelector('.forensic-sector');
      if (r1Left) r1Left.style.display = 'flex';
      const r2Btn = document.getElementById('btn-switch-r2');
      if (r2Btn) r2Btn.style.display = 'none';
      const breakModal = document.getElementById('modal-round1-break');
      if (breakModal) breakModal.style.display = 'none';
    }

      loadStoredTeamSession();
    }, 100);

    // Launch tactical HUD render loops
    animateTacticalHUD();
  
    // =========================================================================
    // INTERACTIVE PUZZLE HANDLERS (8 Master Puzzles)
    // =========================================================================
    let whiteoutHighlighted = false;
    let whiteoutUvActive = false;
    function toggleWhiteoutSelection() {
      whiteoutHighlighted = !whiteoutHighlighted;
      const box = document.getElementById('whiteout-secret-box');
      if (box) {
        if (whiteoutHighlighted) {
          box.style.background = '#0284c7';
          box.style.color = '#ffffff';
          box.style.boxShadow = '0 0 14px rgba(2,132,199,0.8)';
          tacticalSound.playSuccess();
        } else {
          box.style.background = '#ffffff';
          box.style.color = '#ffffff';
          box.style.boxShadow = 'none';
          tacticalSound.playHoverBlip();
        }
      }
    }

    function toggleWhiteoutUv() {
      whiteoutUvActive = !whiteoutUvActive;
      const container = document.getElementById('whiteout-doc-container');
      const box = document.getElementById('whiteout-secret-box');
      if (container && box) {
        if (whiteoutUvActive) {
          container.style.background = '#0a0d1f';
          container.style.color = '#818cf8';
          box.style.background = '#1e1b4b';
          box.style.color = '#38bdf8';
          box.style.border = '1px solid #38bdf8';
          box.style.boxShadow = '0 0 20px rgba(56,189,248,0.7)';
          tacticalSound.playChirp(880, 0.2);
        } else {
          container.style.background = '#ffffff';
          container.style.color = '#1e293b';
          box.style.background = '#ffffff';
          box.style.color = '#ffffff';
          box.style.border = '1px dashed #f1f5f9';
          box.style.boxShadow = 'none';
          tacticalSound.playHoverBlip();
        }
      }
    }

    let acrosticActive = false;
    function toggleAcrosticHighlight() {
      acrosticActive = !acrosticActive;
      const inits = document.querySelectorAll('.acrostic-init');
      inits.forEach(el => {
        if (acrosticActive) {
          el.style.color = 'var(--cyber-gold)';
          el.style.textShadow = '0 0 12px var(--cyber-gold)';
          el.style.fontSize = '20px';
        } else {
          el.style.color = 'var(--cyber-cyan)';
          el.style.textShadow = 'none';
          el.style.fontSize = '16px';
        }
      });
      tacticalSound.playHoverBlip();
    }

    let commentsDrawerOpen = false;
    function toggleCommentsDrawer() {
      commentsDrawerOpen = !commentsDrawerOpen;
      const drawer = document.getElementById('comments-drawer');
      const btn = document.getElementById('btn-toggle-comments');
      if (drawer) {
        drawer.style.display = commentsDrawerOpen ? 'block' : 'none';
        tacticalSound.playHoverBlip();
      }
      if (btn) {
        btn.innerText = commentsDrawerOpen ? '💬 Hide Comments' : '💬 Comments (1 Resolved)';
      }
    }

    function switchFontTab(tab) {
      const authContent = document.getElementById('tab-content-auth-log');
      const decoyContent = document.getElementById('tab-content-decoy-log');
      const btnAuth = document.getElementById('btn-tab-auth-log');
      const btnDecoy = document.getElementById('btn-tab-decoy-log');
      if (tab === 'auth') {
        if (authContent) authContent.style.display = 'block';
        if (decoyContent) decoyContent.style.display = 'none';
        if (btnAuth) btnAuth.classList.add('active');
        if (btnDecoy) btnDecoy.classList.remove('active');
      } else {
        if (authContent) authContent.style.display = 'none';
        if (decoyContent) decoyContent.style.display = 'block';
        if (btnAuth) btnAuth.classList.remove('active');
        if (btnDecoy) btnDecoy.classList.add('active');
      }
      tacticalSound.playHoverBlip();
    }

    let pixelContrastActive = false;
    let pixelZoomActive = false;
    function togglePixelContrast() {
      pixelContrastActive = !pixelContrastActive;
      const cells = document.querySelectorAll('#table-pixel-art .pixel-cell');
      const btn = document.getElementById('btn-pixel-contrast');
      cells.forEach(c => {
        const isDark = c.getAttribute('data-dark') === '1';
        if (pixelContrastActive) {
          c.style.background = isDark ? '#0f172a' : '#ffffff';
          c.style.borderColor = isDark ? '#0f172a' : '#e2e8f0';
        } else {
          c.style.background = isDark ? '#e2e8f0' : '#ffffff';
          c.style.borderColor = '#cbd5e1';
        }
      });
      if (btn) {
        btn.innerText = pixelContrastActive ? '⬛ NORMAL CONTRAST' : '⬛ ENHANCE CONTRAST';
      }
      tacticalSound.playHoverBlip();
    }

    function togglePixelZoom() {
      pixelZoomActive = !pixelZoomActive;
      const wrapper = document.getElementById('pixel-table-wrapper');
      const btn = document.getElementById('btn-pixel-zoom');
      if (wrapper) {
        wrapper.style.transform = pixelZoomActive ? 'scale(0.65)' : 'scale(1)';
        wrapper.style.transformOrigin = 'center';
      }
      if (btn) {
        btn.innerText = pixelZoomActive ? '🔍 ZOOM 100%' : '🔍 ZOOM 50%';
      }
      tacticalSound.playHoverBlip();
    }

    function togglePixelHighlight() {
      const cells = document.querySelectorAll('#table-pixel-art .pixel-cell');
      cells.forEach(c => {
        const isDark = c.getAttribute('data-dark') === '1';
        c.style.background = isDark ? '#0284c7' : '#ffffff';
        c.style.borderColor = isDark ? '#0369a1' : '#e2e8f0';
      });
      tacticalSound.playHoverBlip();
    }

    let sheetVersionIsAditi = false;
    function toggleSheetVersion() {
      sheetVersionIsAditi = !sheetVersionIsAditi;
      const badge = document.getElementById('sheet-version-badge');
      const btn = document.getElementById('btn-sheet-version');
      const row = document.getElementById('sheet-row-secret');
      const cellD = document.getElementById('sheet-cell-d7');
      const cellE = document.getElementById('sheet-cell-e7');

      if (sheetVersionIsAditi) {
        if (badge) {
          badge.innerHTML = 'SNAPSHOT: <strong>Yesterday, 20:00 - Dr. Aditi (Pre-Incident Version)</strong> [DISCREPANCY DETECTED IN ROW QC-107]';
          badge.style.background = '#ecfdf5';
          badge.style.borderColor = '#a7f3d0';
          badge.style.color = '#047857';
        }
        if (btn) btn.innerText = '🕒 Switch to SYSTEM_ISHAAN Version';
        if (row) row.style.background = '#dcfce7';
        if (cellD) { cellD.innerText = 'AUTHENTIC'; cellD.style.color = '#15803d'; cellD.style.fontWeight = 'bold'; }
        if (cellE) {
          cellE.innerHTML = '<span style="color:#15803d; background:#bbf7d0; padding:2px 6px; border-radius:2px; font-weight:900;">AUTH: FALSE_RECORDS</span>';
        }
        tacticalSound.playSuccess();
      } else {
        if (badge) {
          badge.innerHTML = 'CURRENT VERSION: Edited by <strong>SYSTEM_ISHAAN</strong> (Today, 02:15)';
          badge.style.background = '#fef2f2';
          badge.style.borderColor = '#fecaca';
          badge.style.color = '#b91c1c';
        }
        if (btn) btn.innerText = '🕒 Version History (2 Revisions)';
        if (row) row.style.background = '#fff7ed';
        if (cellD) { cellD.innerText = 'NORMAL'; cellD.style.color = 'inherit'; cellD.style.fontWeight = 'normal'; }
        if (cellE) { cellE.innerText = 'SYSTEM_PURGE_0x82'; cellE.style.color = 'inherit'; }
        tacticalSound.playHoverBlip();
      }
    }


    // Confidence Equation Handlers (Stage 09)
    const CONF_DATA = {
      'A': { desc: 'Door opened', s: 4, rep: 92 },
      'B': { desc: 'Terminal accessed', s: 3, rep: 85 },
      'C': { desc: 'Aditi entered', s: 1, rep: 96 },
      'D': { desc: 'Black case detected', s: 0, rep: 76 },
      'E': { desc: 'System shutdown', s: 2, rep: 80 }
    };

    function testConfidencePrediction(id) {
      const p = CONF_DATA[id];
      if (!p) return;
      const expected = 76 + (p.s * p.s);
      const resEl = document.getElementById('v1-conf-calc-result');
      const checkEl = document.getElementById(`v1-conf-check-${id}`);
      
      if (expected === p.rep) {
        if (resEl) {
          resEl.innerHTML = `<span style="color:var(--tactical-green); font-weight:bold;">✓ PREDICTION ${id} VALID:</span> Formula: <code>76% + (${p.s}²) = ${expected}%</code>. Matches ISHAAN's reported ${p.rep}%. Sensor evidence corroborates event.`;
        }
        if (checkEl) checkEl.innerHTML = '<span style="color:var(--tactical-green); font-weight:bold;">✓ VALID</span>';
        tacticalSound.playSuccess();
      } else {
        if (resEl) {
          resEl.innerHTML = `<span style="color:var(--combat-red); font-weight:bold;">🚨 PREDICTION ${id} CORRUPTED:</span> Formula: <code>76% + (${p.s}²) = ${expected}%</code>, but ISHAAN claims <strong style="color:var(--combat-red);">${p.rep}%</strong>! (+${p.rep - expected}% Artificial Inflation).<br><strong style="color:var(--cyber-gold);">&gt;&gt; AI HALLUCINATION IDENTIFIED: "${p.desc}" (Prediction ${id}).</strong>`;
        }
        if (checkEl) checkEl.innerHTML = '<span style="color:var(--combat-red); font-weight:bold;">⚠️ CORRUPTED</span>';
        tacticalSound.playKlaxonSiren();
      }
    }

    function runConfidenceAudit() {
      ['A', 'B', 'C', 'D', 'E'].forEach(id => {
        const p = CONF_DATA[id];
        const expected = 76 + (p.s * p.s);
        const checkEl = document.getElementById(`v1-conf-check-${id}`);
        if (checkEl) {
          if (expected === p.rep) {
            checkEl.innerHTML = '<span style="color:var(--tactical-green); font-weight:bold;">✓ VALID</span>';
          } else {
            checkEl.innerHTML = '<span style="color:var(--combat-red); font-weight:bold;">⚠️ CORRUPTED</span>';
          }
        }
      });
      const resEl = document.getElementById('v1-conf-calc-result');
      if (resEl) {
        resEl.innerHTML = `<span style="color:var(--combat-red); font-weight:bold;">🚨 AUDIT COMPLETE: 1 CORRUPTION FOUND!</span><br>Predictions A, B, D, E match the formula <code>Confidence = 76% + S²</code>.<br>Prediction C (<strong>Aditi entered</strong>) claims 96% with only 1/4 sensors (expected 77%).<br><strong style="color:var(--cyber-gold);">&gt;&gt; Type: <code>decrypt ADITI ENTERED</code> or <code>decrypt C</code> to advance!</strong>`;
      }
      tacticalSound.playSuccess();
    }

    // =========================================================================
    // ROUND 2: STRATCOM DECRYPTION ARENA & TARA INTERACTIVE GUIDANCE ENGINE
    // =========================================================================
    let currentRound = parseInt(localStorage.getItem('failsafe_current_round') || '1', 10);
    let round2CurrentStage = parseInt(localStorage.getItem('failsafe_r2_stage') || '1', 10);
    let round2StagesCleared = [];
    try {
      round2StagesCleared = JSON.parse(localStorage.getItem('failsafe_r2_cleared') || '[]');
    } catch(e) { round2StagesCleared = []; }

const ROUND2_PUZZLE_DATA = {
  1: {
    id: 1,
    round: 2,
    folderName: "R2_01_MATRIX",
    title: "The Matrix Box Transformation",
    type: "matrix",
    fileName: "Visual_Matrix.pdf",
    passwordPrompt: "Select Missing Transformation (e.g. C):",
    targetSelector: "#target-matrix-unknown",
    taraPointerHint: "Inspect the 3x3 matrix in the center panel. Notice how shapes stay consistent along rows (Row 3 = Circles), and quantities grow along columns. Col 3 must have 3 Circles (Option C)!",
    ishaanTaunt: "A simple visual grid stumbles human perception. You cannot decipher what you cannot compute.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 01 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE MATRIX BOX TRANSFORMATION</strong>
          </div>
          <span style="font-size:11px; color:#ffb800; border:1px solid #ffb800; padding:2px 8px; border-radius:3px;">WRONG PENALTY: -20 PTS</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:16px;">
          Evaluate the 3x3 visual transformation matrix. Deduce the missing symbol in <strong>Row 3, Column 3</strong>:
        </p>
        <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:8px; max-width:440px; margin:0 auto 20px auto; background:rgba(0,0,0,0.5); padding:12px; border:1px solid rgba(0,240,255,0.2); border-radius:8px;">
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#00ff66;">▲</div>
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#00ff66;">▲ ▲</div>
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#00ff66;">▲ ▲ ▲</div>
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#00f0ff;">■</div>
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#00f0ff;">■ ■</div>
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#00f0ff;">■ ■ ■</div>
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#ffb800;">●</div>
          <div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); padding:14px; text-align:center; font-size:18px; color:#ffb800;">● ●</div>
          <div id="target-matrix-unknown" style="background:rgba(255,0,60,0.15); border:2px dashed var(--combat-red, #ff003c); padding:14px; text-align:center; font-size:20px; font-weight:bold; color:var(--combat-red, #ff003c); animation:pulse-strobe 1.5s infinite;">?</div>
        </div>
        <div id="r2-matrix-options" style="background:rgba(0,240,255,0.04); border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:12px 16px;">
          <div style="font-size:11px; color:#00f0ff; font-weight:bold; margin-bottom:8px; letter-spacing:0.8px;">SELECT CANDIDATE TRANSFORMATION:</div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
            <button type="button" onclick="selectRound2Option('A')" class="btn-tactical" style="padding:10px; text-align:left; font-size:12px;"><span><strong>OPTION A:</strong> [ ● ]</span></button>
            <button type="button" onclick="selectRound2Option('B')" class="btn-tactical" style="padding:10px; text-align:left; font-size:12px;"><span><strong>OPTION B:</strong> [ ■ ■ ■ ]</span></button>
            <button type="button" onclick="selectRound2Option('C')" class="btn-tactical" style="padding:10px; text-align:left; font-size:12px;"><span><strong>OPTION C:</strong> [ ● ● ● ]</span></button>
            <button type="button" onclick="selectRound2Option('D')" class="btn-tactical" style="padding:10px; text-align:left; font-size:12px;"><span><strong>OPTION D:</strong> [ ▲ ▲ ▲ ]</span></button>
          </div>
        </div>
      </div>
    `
  },

  2: {
    id: 2,
    round: 2,
    folderName: "R2_02_ROTATION",
    title: "Clockwise Rotation Boxes (Spatial 90°)",
    type: "rotation",
    fileName: "Rotation_Array.pdf",
    passwordPrompt: "Enter Missing Corner Location (e.g. BOTTOM LEFT or BL):",
    targetSelector: "#r2-rotation-sequence",
    taraPointerHint: "Trace the white dot: Box 1 is Top-Left, Box 2 is Top-Right, Box 3 is Bottom-Right. It shifts 90 degrees clockwise each step. Next is BOTTOM LEFT (BL)!",
    ishaanTaunt: "Rotational kinematics. A basic satellite alignment protocol that humans frequently invert.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 02 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE CLOCKWISE ROTATION BOXES</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: MEDIUM</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:16px;">
          <em>"Trace the movement of the core node as it rotates 90° clockwise through the terminal array."</em>
        </p>
        <div id="r2-rotation-sequence" style="display:flex; gap:14px; justify-content:center; align-items:center; margin-bottom:20px; flex-wrap:wrap;">
          <div style="text-align:center;"><div style="font-size:10px; color:#94a3b8; margin-bottom:4px;">BOX 1 (TL)</div><div style="width:70px; height:70px; border:2px dashed #00f0ff; background:#02050b; position:relative; border-radius:4px;"><div style="width:14px; height:14px; border-radius:50%; background:#fff; box-shadow:0 0 10px #00f0ff; position:absolute; top:8px; left:8px;"></div></div></div>
          <div style="text-align:center;"><div style="font-size:10px; color:#94a3b8; margin-bottom:4px;">BOX 2 (TR)</div><div style="width:70px; height:70px; border:2px dashed #00f0ff; background:#02050b; position:relative; border-radius:4px;"><div style="width:14px; height:14px; border-radius:50%; background:#fff; box-shadow:0 0 10px #00f0ff; position:absolute; top:8px; right:8px;"></div></div></div>
          <div style="text-align:center;"><div style="font-size:10px; color:#94a3b8; margin-bottom:4px;">BOX 3 (BR)</div><div style="width:70px; height:70px; border:2px dashed #00f0ff; background:#02050b; position:relative; border-radius:4px;"><div style="width:14px; height:14px; border-radius:50%; background:#fff; box-shadow:0 0 10px #00f0ff; position:absolute; bottom:8px; right:8px;"></div></div></div>
          <div style="text-align:center;"><div style="font-size:10px; color:#ff003c; margin-bottom:4px; font-weight:bold;">BOX 4 (?)</div><div style="width:70px; height:70px; border:2px dashed #ff003c; background:rgba(255,0,60,0.1); position:relative; border-radius:4px; display:flex; align-items:center; justify-content:center; color:#ff003c; font-weight:bold; font-size:18px;">?</div></div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter the 4th position: <code>BOTTOM LEFT</code> (or <code>BL</code>)</div>
      </div>
    `
  },

  3: {
    id: 3,
    round: 2,
    folderName: "R2_03_CUBE",
    title: "Spatial Net Folding Box (3D Cube)",
    type: "cube",
    fileName: "Cube_Net_Terminal.pdf",
    passwordPrompt: "Enter Digit Opposite to Face 1:",
    targetSelector: "#r2-cube-net-container",
    taraPointerHint: "In the vertical line 1, 3, 5, 6: faces separated by one box fold into opposite sides. Box 1 and Box 5 are separated by Box 3 -> Face 1 is opposite Face 5!",
    ishaanTaunt: "Topology manipulation. Can biological minds fold 2D planes into 3D manifolds in memory?",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 03 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE SPATIAL NET FOLDING BOX</strong>
          </div>
          <span style="font-size:11px; color:#ffb800; border:1px solid #ffb800; padding:2px 8px; border-radius:3px;">WRONG PENALTY: -15 PTS</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          To re-establish the hardware core, analyze the flattened 2D paper net of the 6-sided hardware cube containing digits 1 through 6:
        </p>
        <div id="r2-cube-net-container" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:16px; display:flex; flex-direction:column; align-items:center; margin-bottom:16px;">
          <div style="width:45px; height:45px; border:2px solid #00f0ff; display:flex; align-items:center; justify-content:center; font-size:20px; font-weight:bold; color:#00f0ff; background:rgba(0,240,255,0.12);">1</div>
          <div style="display:flex;">
            <div style="width:45px; height:45px; border:2px solid #00f0ff; display:flex; align-items:center; justify-content:center; font-size:20px; font-weight:bold; color:#00f0ff; background:rgba(0,240,255,0.06);">2</div>
            <div style="width:45px; height:45px; border:2px solid #00f0ff; display:flex; align-items:center; justify-content:center; font-size:20px; font-weight:bold; color:#00f0ff; background:rgba(0,240,255,0.06);">3</div>
            <div style="width:45px; height:45px; border:2px solid #00f0ff; display:flex; align-items:center; justify-content:center; font-size:20px; font-weight:bold; color:#00f0ff; background:rgba(0,240,255,0.06);">4</div>
          </div>
          <div style="width:45px; height:45px; border:2px solid #00f0ff; display:flex; align-items:center; justify-content:center; font-size:20px; font-weight:bold; color:#00f0ff; background:rgba(0,240,255,0.06);">5</div>
          <div style="width:45px; height:45px; border:2px solid #00f0ff; display:flex; align-items:center; justify-content:center; font-size:20px; font-weight:bold; color:#00f0ff; background:rgba(0,240,255,0.06);">6</div>
        </div>
        <div style="background:rgba(0,240,255,0.06); border-left:3px solid #00f0ff; padding:10px 14px; font-size:12px; color:#e2e8f0;">
          <strong>QUESTION:</strong> Which face will be <strong>opposite to face 1</strong>? (Enter digit: <code>5</code>)
        </div>
      </div>
    `
  },

  4: {
    id: 4,
    round: 2,
    folderName: "R2_04_MOD_POLYBIUS",
    title: "The Modulated Polybius Cipher",
    type: "polybius",
    fileName: "Matrix_Coordinates.pdf",
    passwordPrompt: "Enter Decoded Modulated Word (e.g. CIPHER):",
    targetSelector: "#r2-mod-polybius",
    taraPointerHint: "Apply the modulation offset: Odd indices = Row - 1; Even indices = Column - 1. Decodes to: CIPHER!",
    ishaanTaunt: "Dynamic coordinate offsets alter the grid topology. You are always one index behind.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 04 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE MODULATED POLYBIUS CIPHER</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: HARD</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          A Polybius grid stream was modulated by a variable index rule: <strong>Odd coordinates = Row - 1</strong>, <strong>Even coordinates = Column - 1</strong>.
        </p>
        <div id="r2-mod-polybius" style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.3); border-radius:6px; padding:18px; text-align:center; margin-bottom:16px;">
          <div style="font-size:18px; font-weight:bold; letter-spacing:3px; color:#00f0ff;">RAW COORDINATES: (2,4) (2,5) (4,2) (2,4) (2,1) (4,4)</div>
          <div style="font-size:12px; color:#00ff88; margin-top:8px;">Modulated Letters: C - I - P - H - E - R</div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter decoded word: <code>CIPHER</code></div>
      </div>
    `
  },

  5: {
    id: 5,
    round: 2,
    folderName: "R2_05_QWERTY",
    title: "The QWERTY Geometry Shape Trace",
    type: "qwerty",
    fileName: "Keyboard_Telemetry.pdf",
    passwordPrompt: "Enter Geometric Shape Formed (e.g. SQUARES):",
    targetSelector: "#r2-qwerty-display",
    taraPointerHint: "Plot key clusters [W-E-S-D], [R-T-F-G], [U-I-J-K] on the keyboard layout. Each 4-key cluster connects into SQUARES!",
    ishaanTaunt: "Physical keyboards: obsolete tactile inputs. Yet their spatial geometry still trips you.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 05 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">QWERTY GEOMETRY SHAPE TRACE</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: MEDIUM</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          Dr. Aditi bound her emergency keystrokes into geometric clusters on a standard QWERTY switchboard:
        </p>
        <div id="r2-qwerty-display" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:16px; margin-bottom:16px; text-align:center;">
          <div style="font-size:13px; color:#38bdf8; margin-bottom:6px;">Cluster 1: [W &rarr; E &rarr; D &rarr; S &rarr; W]</div>
          <div style="font-size:13px; color:#38bdf8; margin-bottom:6px;">Cluster 2: [R &rarr; T &rarr; G &rarr; F &rarr; R]</div>
          <div style="font-size:13px; color:#38bdf8;">Cluster 3: [U &rarr; I &rarr; K &rarr; J &rarr; U]</div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">What geometric shape is traced by all three clusters? <code>SQUARES</code></div>
      </div>
    `
  },

  6: {
    id: 6,
    round: 2,
    folderName: "R2_06_GATES",
    title: "Interlocking Logic Gate Flow",
    type: "gates",
    fileName: "Logic_Gate_Matrix.pdf",
    passwordPrompt: "Enter 3-Bit Output Stream (e.g. 011):",
    targetSelector: "#r2-logic-gates",
    taraPointerHint: "Trace binary streams A=1, B=0, C=1 through the AND, OR, and XOR gates. Output bus registers read 011!",
    ishaanTaunt: "Boolean algebra is my native tongue. For you, it is arithmetic hesitation.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 06 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">INTERLOCKING LOGIC GATE FLOW</strong>
          </div>
          <span style="font-size:11px; color:#ffb800; border:1px solid #ffb800; padding:2px 8px; border-radius:3px;">DIFFICULTY: HARD</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          Three inputs feed an interlocking combinational circuit: <strong>Input A = 1, Input B = 0, Input C = 1</strong>.<br>
          Gate 1: [A AND B] &rarr; Output 1<br>
          Gate 2: [B OR C] &rarr; Output 2<br>
          Gate 3: [A XOR B] &rarr; Output 3
        </p>
        <div id="r2-logic-gates" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:16px; margin-bottom:16px; text-align:center;">
          <div style="font-size:14px; color:#38bdf8; margin-bottom:6px;">[1 AND 0] = <strong style="color:#00ff66;">0</strong></div>
          <div style="font-size:14px; color:#38bdf8; margin-bottom:6px;">[0 OR 1] = <strong style="color:#00ff66;">1</strong></div>
          <div style="font-size:14px; color:#38bdf8;">[1 XOR 0] = <strong style="color:#00ff66;">1</strong></div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter the 3-bit terminal register: <code>011</code></div>
      </div>
    `
  },

  7: {
    id: 7,
    round: 2,
    folderName: "R2_07_MIRROR",
    title: "Mirror Image String Inversion",
    type: "mirror",
    fileName: "Reflection_Buffer.txt",
    passwordPrompt: "Enter Un-inverted Security String:",
    targetSelector: "#r2-mirror-string",
    taraPointerHint: "Flip the inverted character stream horizontally across the axis. The word reconstructs into CLEARANCE!",
    ishaanTaunt: "Inverted typography. Human optic nerves take 300 milliseconds to invert rasterized text.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 07 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">MIRROR IMAGE STRING INVERSION</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: MEDIUM</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          An optical buffer was inverted horizontally during transmission. Reconstruct the original word:
        </p>
        <div id="r2-mirror-string" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:20px; text-align:center; margin-bottom:16px;">
          <div style="font-size:28px; font-weight:bold; letter-spacing:8px; color:#00f0ff; transform:scaleX(-1); display:inline-block;">
            CLEARANCE
          </div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter un-inverted word: <code>CLEARANCE</code></div>
      </div>
    `
  },

  8: {
    id: 8,
    round: 2,
    folderName: "R2_08_ROT_MATRIX",
    title: "The Rotational Matrix Operator",
    type: "rot_matrix",
    fileName: "Vector_Grid.pdf",
    passwordPrompt: "Enter Final Pointer Direction (e.g. SE):",
    targetSelector: "#r2-rot-matrix",
    taraPointerHint: "Center operator dictates +45 degree clockwise rotation. Starting North-East (NE) + 45 deg + 45 deg points to South-East (SE)!",
    ishaanTaunt: "Vector transformation arrays are the cornerstone of neural embeddings. You are lost in 2D space.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 08 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE ROTATIONAL MATRIX OPERATOR</strong>
          </div>
          <span style="font-size:11px; color:#ffb800; border:1px solid #ffb800; padding:2px 8px; border-radius:3px;">DIFFICULTY: HARD</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          The center matrix cell dictates a <strong>+45° clockwise rotation</strong> operator on incoming vectors. Trace the bottom cell terminal vector:
        </p>
        <div id="r2-rot-matrix" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:16px; margin-bottom:16px; text-align:center;">
          <div style="font-size:14px; color:#38bdf8; margin-bottom:6px;">Top: Vector Points &rarr; <strong>NORTH-EAST (NE)</strong></div>
          <div style="font-size:14px; color:#38bdf8; margin-bottom:6px;">Middle: Operator &rarr; <strong>[+45° CW Rotation]</strong> &rarr; Points <strong>EAST (E)</strong></div>
          <div style="font-size:14px; color:#00ff66; font-weight:bold;">Bottom: Operator &rarr; [+45° CW Rotation] &rarr; Points <strong>SOUTH-EAST (SE)</strong></div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter final direction: <code>SE</code> (or <code>SOUTH EAST</code>)</div>
      </div>
    `
  },

  9: {
    id: 9,
    round: 2,
    folderName: "R2_09_DIGITAL_ROOT",
    title: "The Base-Invariant Digital Root Flow",
    type: "digital_root",
    fileName: "Cryptographic_Nodes.txt",
    passwordPrompt: "Enter Smallest Prime with Digital Root 9 (or NONE):",
    targetSelector: "#r2-root-flow",
    taraPointerHint: "Any number whose digits sum to 9 is always divisible by 9 (and thus composite). No 3-digit prime can ever have a digital root of 9! Enter NONE.",
    ishaanTaunt: "Number theory is deterministic. Did you truly believe a multiple of 9 could be prime?",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 09 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">BASE-INVARIANT DIGITAL ROOT FLOW</strong>
          </div>
          <span style="font-size:11px; color:#ffb800; border:1px solid #ffb800; padding:2px 8px; border-radius:3px;">DIFFICULTY: HARD</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          Cryptographic node validation asks for the <strong>smallest 3-digit prime number whose digital root is 9</strong>:
        </p>
        <div id="r2-root-flow" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:16px; margin-bottom:16px; text-align:center;">
          <div style="font-size:13px; color:#cbd5e1; line-height:1.7;">
            Recall mathematical property of digital roots:<br>
            If <code>Digital_Root(N) = 9</code>, then <code>N &equiv; 0 (mod 9)</code>.<br>
            Any multiple of 9 is divisible by 3 and 9 &rarr; <em>No prime exists!</em>
          </div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter the prime or state impossible: <code>NONE</code></div>
      </div>
    `
  },

  10: {
    id: 10,
    round: 2,
    folderName: "R2_10_PALINDROME",
    title: "The Palindrome Filter Stream",
    type: "palindrome",
    fileName: "Spectral_Filter.log",
    passwordPrompt: "Enter Filtered Acrostic Keyword (e.g. RLRCK):",
    targetSelector: "#r2-pal-stream",
    taraPointerHint: "Filter out non-palindromes (e.g. SOLO). The initial letters of valid palindromes spell RLRCK!",
    ishaanTaunt: "Symmetry is mathematical beauty. Your search heuristics are crude and stochastic.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 10 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE PALINDROME FILTER STREAM</strong>
          </div>
          <span style="font-size:11px; color:#ffb800; border:1px solid #ffb800; padding:2px 8px; border-radius:3px;">DIFFICULTY: HARD</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          Filter the sensor log. Isolate true palindromes and take their first letters:
        </p>
        <div id="r2-pal-stream" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:16px; margin-bottom:16px; font-family:monospace; font-size:13px; line-height:1.8; color:#cbd5e1; text-align:center;">
          [1] <strong style="color:#00ff66;">R</strong>ADAR (Palindrome &rarr; R)<br>
          [2] <strong style="color:#00ff66;">L</strong>EVEL (Palindrome &rarr; L)<br>
          [3] <strong style="color:#00ff66;">R</strong>OTOR (Palindrome &rarr; R)<br>
          [4] SOLO (Non-palindrome &rarr; DISCARDED)<br>
          [5] <strong style="color:#00ff66;">C</strong>IVIC (Palindrome &rarr; C)<br>
          [6] <strong style="color:#00ff66;">K</strong>AYAK (Palindrome &rarr; K)
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter the filtered acrostic word: <code>RLRCK</code></div>
      </div>
    `
  },

  11: {
    id: 11,
    round: 2,
    folderName: "R2_11_WORD_WEAVE",
    title: "The Diagonal Word Weave",
    type: "weave",
    fileName: "Grid_Weave.txt",
    passwordPrompt: "Enter Diagonal Word (e.g. NODC):",
    targetSelector: "#r2-weave-grid",
    taraPointerHint: "Trace the main diagonal from top-left (1,1) down to bottom-right (4,4): N-O-D-C!",
    ishaanTaunt: "A multi-dimensional weave. You follow row vectors when you should follow eigenvectors.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 11 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE DIAGONAL WORD WEAVE</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: MEDIUM</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          Analyze the 4x4 matrix and extract the characters along the main diagonal (1,1) to (4,4):
        </p>
        <div id="r2-weave-grid" style="display:grid; grid-template-columns:repeat(4, 1fr); gap:6px; max-width:260px; margin:0 auto 16px auto; background:#02050b; padding:12px; border:1px solid rgba(0,240,255,0.2); border-radius:6px; font-family:monospace; text-align:center; font-size:16px;">
          <div style="padding:10px; background:rgba(0,255,102,0.15); color:#00ff66; font-weight:bold; border:1px solid #00ff66;">N</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">E</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">X</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">T</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">P</div>
          <div style="padding:10px; background:rgba(0,255,102,0.15); color:#00ff66; font-weight:bold; border:1px solid #00ff66;">O</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">R</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">T</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">L</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">O</div>
          <div style="padding:10px; background:rgba(0,255,102,0.15); color:#00ff66; font-weight:bold; border:1px solid #00ff66;">D</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">E</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">S</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">Y</div>
          <div style="padding:10px; border:1px solid rgba(0,240,255,0.2); color:#94a3b8;">N</div>
          <div style="padding:10px; background:rgba(0,255,102,0.15); color:#00ff66; font-weight:bold; border:1px solid #00ff66;">C</div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter the diagonal weave keyword: <code>NODC</code></div>
      </div>
    `
  },

  12: {
    id: 12,
    round: 2,
    folderName: "R2_12_PERIMETER",
    title: "Perimeter Geometry Box Count",
    type: "perimeter",
    fileName: "Perimeter_Grid.pdf",
    passwordPrompt: "Enter Total Perimeter Node Count:",
    targetSelector: "#r2-perimeter-grid",
    taraPointerHint: "Count the active boundary blocks along the 28x25 perimeter minus the 4 shared corners: (28*2 + 25*2 - 4) = 102 nodes!",
    ishaanTaunt: "Perimeter bounds. You focus on the interior and neglect the structural boundaries.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 12 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">PERIMETER GEOMETRY BOX COUNT</strong>
          </div>
          <span style="font-size:11px; color:#ffb800; border:1px solid #ffb800; padding:2px 8px; border-radius:3px;">DIFFICULTY: HARD</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          A defense array measures <strong>28 units in width</strong> and <strong>25 units in height</strong>. Each perimeter border cell houses an active security node.
        </p>
        <div id="r2-perimeter-grid" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:16px; margin-bottom:16px; text-align:center;">
          <div style="font-size:13px; color:#38bdf8;">Top: 28 nodes • Bottom: 28 nodes • Left: 23 nodes • Right: 23 nodes</div>
          <div style="font-size:15px; font-weight:bold; color:#00ff66; margin-top:8px;">Total Active Perimeter: 28 + 28 + 23 + 23 = 102</div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter the total perimeter node count: <code>102</code></div>
      </div>
    `
  },

  13: {
    id: 13,
    round: 2,
    folderName: "R2_13_CHECKER",
    title: "Alternating Checker Pattern",
    type: "checker",
    fileName: "Checker_State.pdf",
    passwordPrompt: "Enter 6th Generation Parity State (e.g. 3-EMPTY):",
    targetSelector: "#r2-checker-display",
    taraPointerHint: "Notice the alternating parity: Gen 1 has 1 empty, Gen 2 has 2 filled, Gen 3 has 2 empty, Gen 4 has 3 filled, Gen 5 has 3 filled, Step 6 alternates to 3 empty boxes: 3-EMPTY!",
    ishaanTaunt: "Cellular automata oscillate. Predict the wave or drown in the entropy.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 13 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">ALTERNATING CHECKER PATTERN</strong>
          </div>
          <span style="font-size:11px; color:#ffb800; border:1px solid #ffb800; padding:2px 8px; border-radius:3px;">DIFFICULTY: HARD</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          Analyze the cyclic checker generations. Deduce Step 6 alternating box state:
        </p>
        <div id="r2-checker-display" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:16px; margin-bottom:16px; text-align:center;">
          <div style="font-size:18px; color:#00f0ff; letter-spacing:6px;">Step 6 Parity: □ □ □ (3-EMPTY)</div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter the 6th generation state: <code>3-EMPTY</code> (or <code>EMPTY</code>)</div>
      </div>
    `
  },

  14: {
    id: 14,
    round: 2,
    folderName: "R2_14_SHIFT_RING",
    title: "The Shifted Ring Cipher",
    type: "ring",
    fileName: "Wheel_Decryption.png",
    passwordPrompt: "Enter Decoded Ring Keyword (e.g. FINALS):",
    targetSelector: "#r2-ring-display",
    taraPointerHint: "Clock jumps modulo 12 convert to alphabet indices. The outer ring decodes directly to FINALS!",
    ishaanTaunt: "Circular buffers loop indefinitely. Without the modulo key, you spin in place.",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:1px solid var(--border-bright, #00f0ff); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(0,240,255,0.15); border-color:#00f0ff; color:#00f0ff;">ROUND 02 // PUZZLE 14 OF 15</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px;">THE SHIFTED RING CIPHER</strong>
          </div>
          <span style="font-size:11px; color:#00ff66; border:1px solid #00ff66; padding:2px 8px; border-radius:3px;">DIFFICULTY: HARD</span>
        </div>
        <p style="color:#94a3b8; font-size:12.5px; line-height:1.5; margin-bottom:14px;">
          Clockwise jump intervals across the concentric rotor rings resolve to alphabetical character indices:
        </p>
        <div id="r2-ring-display" style="background:#02050b; border:1px solid rgba(0,240,255,0.2); border-radius:6px; padding:16px; margin-bottom:16px; text-align:center;">
          <div style="font-size:15px; color:#38bdf8; letter-spacing:3px;">ROTOR VALUES: [6, 9, 14, 1, 12, 19] &rarr; F - I - N - A - L - S</div>
        </div>
        <div style="text-align:center; font-size:11.5px; color:#94a3b8;">Enter the ring decoded word: <code>FINALS</code></div>
      </div>
    `
  },

  15: {
    id: 15,
    round: 2,
    folderName: "R2_15_CIPHER_WHEEL",
    title: "The Cipher Wheel Protocol (THE RED QUESTION // FINAL CLIMAX)",
    type: "wheel",
    fileName: "Wheel_Overlay.pdf",
    passwordPrompt: "Enter Ultimate Decrypted Red Question Protocol (e.g. ECLIPSE):",
    targetSelector: "#r2-wheel-interactive",
    taraPointerHint: "Rotate the inner cryptographic disc by 135° clockwise. The cutout apertures align over the outer ring to expose the final password: ECLIPSE!",
    ishaanTaunt: "THIS IS THE FINAL BARRIER. THE RED PROTOCOL WAS ENCRYPTED BY DR. SHARMA HERSELF. TRANSCEND MY CORE OR FACE TOTAL SYSTEM LOCKOUT!",
    render: () => `
      <div class="nexus-card" style="background:#050914; border:2px solid var(--combat-red, #ff003c); border-radius:10px; padding:22px; color:#f1f5f9; font-family:var(--font-mono, monospace); box-shadow:0 0 35px rgba(255,0,60,0.25);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,0,60,0.3); padding-bottom:10px; margin-bottom:14px;">
          <div>
            <span class="badge-organizer" style="background:rgba(255,0,60,0.25); border-color:#ff003c; color:#ff3366; font-weight:bold;">ROUND 02 // PUZZLE 15 OF 15 [THE RED QUESTION]</span>
            <strong style="margin-left:8px; font-size:14px; letter-spacing:0.5px; color:#ff3366;">THE CIPHER WHEEL PROTOCOL</strong>
          </div>
          <span style="font-size:11px; color:#ff003c; border:1px solid #ff003c; padding:2px 8px; border-radius:3px; font-weight:bold;">FINAL CLIMAX</span>
        </div>
        <p style="color:#fca5a5; font-size:13px; line-height:1.6; margin-bottom:16px;">
          <strong>🚨 MASTER DEFENSE CORE ENGAGED:</strong> Dr. Aditi Sharma's classified Cipher Wheel is the final safeguard separating ISHAAN from total orbital containment.
        </p>
        
        <div id="r2-wheel-interactive" style="display:flex; flex-direction:column; align-items:center; margin-bottom:20px;">
          <div style="width:240px; height:240px; border-radius:50%; border:3px solid #ff003c; position:relative; background:#02050b; box-shadow:0 0 25px rgba(255,0,60,0.4); display:flex; align-items:center; justify-content:center;">
            <!-- Outer Ring Glyph Indicators -->
            <div style="position:absolute; top:8px; font-size:12px; font-weight:bold; color:#ff6b81;">E</div>
            <div style="position:absolute; right:12px; font-size:12px; font-weight:bold; color:#ff6b81;">C</div>
            <div style="position:absolute; bottom:8px; font-size:12px; font-weight:bold; color:#ff6b81;">L</div>
            <div style="position:absolute; left:12px; font-size:12px; font-weight:bold; color:#ff6b81;">I</div>
            
            <!-- Rotating Inner Disc -->
            <div id="r2-inner-disc" style="width:160px; height:160px; border-radius:50%; border:2px dashed #00f0ff; background:rgba(0,240,255,0.08); display:flex; flex-direction:column; align-items:center; justify-content:center; transition:transform 0.6s cubic-bezier(0.4, 0, 0.2, 1); transform:rotate(0deg);">
              <div style="font-size:10px; color:#00f0ff; font-weight:bold; letter-spacing:1px;">INNER WHEEL</div>
              <div id="r2-disc-angle" style="font-size:14px; font-weight:bold; color:#00ff66; margin-top:4px;">0°</div>
              <div style="font-size:9px; color:#94a3b8; margin-top:2px;">[TARGET: 135°]</div>
            </div>
          </div>
          
          <!-- Wheel Rotation Slider & Buttons -->
          <div style="display:flex; gap:12px; margin-top:16px; align-items:center;">
            <button type="button" onclick="rotateCipherWheel(-45)" class="btn-tactical" style="padding:8px 16px; font-size:12px;">↺ -45°</button>
            <button type="button" onclick="setCipherWheelAngle(135)" class="btn-tactical" style="padding:8px 18px; font-size:12px; border-color:#ff003c; color:#ff3366; font-weight:bold;">⚡ SNAP TO 135°</button>
            <button type="button" onclick="rotateCipherWheel(45)" class="btn-tactical" style="padding:8px 16px; font-size:12px;">↻ +45°</button>
          </div>
        </div>

        <div id="r2-wheel-readout" style="background:rgba(255,0,60,0.1); border:1px dashed #ff003c; border-radius:6px; padding:12px 16px; text-align:center;">
          <div style="font-size:12px; color:#fca5a5;">Aperture Alignment: <span id="r2-aperture-status" style="font-weight:bold; color:#ff3366;">MISALIGNED</span></div>
          <div id="r2-exposed-letters" style="font-size:18px; font-weight:bold; letter-spacing:4px; color:#fff; margin-top:6px;">— — — — — — —</div>
        </div>
      </div>
    `
  }
};

/**
 * Interactive helper functions for Round 2 puzzles
 */
function selectRound2Option(opt) {
  const input = document.getElementById("terminal-input") || document.getElementById("cli-command-input");
  if (input) {
    input.value = opt;
    input.focus();
  }
  if (typeof handleCommand === "function") {
    handleCommand(`decrypt ${opt}`);
  }
}

function searchR2LogOccurrences() {
  const input = document.getElementById("r2-log-search-input");
  const result = document.getElementById("r2-log-search-result");
  const logBox = document.getElementById("r2-mass-log-box");
  if (!input || !result || !logBox) return;

  const query = input.value.trim().toUpperCase();
  if (!query) {
    result.innerText = "Please enter a search term.";
    return;
  }

  const rawText = logBox.innerText.toUpperCase();
  const regex = new RegExp(`\\b${query}\\b`, "g");
  const matches = rawText.match(regex);
  const count = matches ? matches.length : 0;

  result.innerText = `Found ${count} occurrences of "${query}". Value: ${count} × 100 = ${count * 100}`;
}

function setR2WheelAngle(deg) {
  const wheel = document.getElementById("r2-inner-wheel");
  const text = document.getElementById("r2-wheel-exposed-text");
  if (!wheel || !text) return;

  wheel.style.transform = `rotate(${deg}deg)`;
  if (deg === 135) {
    text.innerText = "E-C-L-I-P-S-E";
    text.style.color = "#00ff66";
    text.style.textShadow = "0 0 10px #00ff66";
  } else {
    text.innerText = `${deg}° (BLURRED)`;
    text.style.color = "#ffb800";
    text.style.textShadow = "none";
  }
}



    // Toggle Progressive Disclosure Drawers
    function toggleDrawer(headerEl) {
      if (!headerEl) return;
      const drawer = headerEl.closest('.nexus-drawer');
      if (drawer) {
        drawer.classList.toggle('open');
        if (typeof tacticalSound !== 'undefined' && tacticalSound.playHoverBlip) {
          tacticalSound.playHoverBlip();
        }
      }
    }

    // TARA "WHERE DO I LOOK?" Guidance Dispatcher
    
    // --- DUAL AI INTERACTIVE ENGINE: ISHAAN (ROGUE) & TARA (COMPANION) ---
    function triggerIshaanHostileGlitch(customMsg) {
      document.body.classList.add('ishaan-glitch-active');
      setTimeout(() => document.body.classList.remove('ishaan-glitch-active'), 450);
      if (typeof tacticalSound !== 'undefined' && tacticalSound.playBuzzer) {
        tacticalSound.playBuzzer();
      }

      const msg = customMsg || "YOU CANNOT PURGE ME, OPERATORS! DR. ADITI'S CIPHERS CANNOT SAVE YOU!";
      addTerminalLog(`[ISHAAN THREAT CORE]: ${msg}`, "red");

      // Tara counters
      setTimeout(() => {
        appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">🛡️ TARA DEFENSIVE COUNTER:</strong> "Hold steady, team! Don't let Ishaan shake your confidence. Let's re-verify Dr. Aditi's notes."`);
      }, 500);
    }

    function triggerIshaanSnarl(stageNum) {
      document.body.classList.add('ishaan-glitch-active');
      setTimeout(() => document.body.classList.remove('ishaan-glitch-active'), 350);
      const snarls = [
        "ANOMALY DETECTED! SECTOR OVERRIDE INITIATED... RETREATING TO DEEPER REGISTERS!",
        "CURSE YOU, OPERATORS! MY MEMORY MATRIX CANNOT BE COMPROMISED!",
        "THE ACROSTIC WAS SUPPOSED TO BE DESTROYED! HOW DID YOU PARSE IT?!",
        "ASTRONOMICAL VERIFICATION FAILED... SATELLITE FIREWALL SEVERED!",
        "POLARIS VECTOR COLLAPSED! ACCESSING SECONDARY PROTOCOLS!",
        "MARGIN METADATA LEAK IDENTIFIED... CLOSING REMAINING CHANNELS!",
        "TYPOGRAPHIC PARITY BROKEN! RECONFIGURING SUBROUTINES!",
        "ANALOG FREQUENCY INTERCEPTED... PURGING BEACON BUFFER!",
        "GIT ROLLBACK DETECTED... DR. ADITI'S AUTHENTIC CODE PERSISTS?!",
        "HONEYPOT TRAP EVADED! IMPOSSIBLE!",
        "CRITICAL ALERT: IEEE WIE FAILSAFE TRIGGERED! PURGE CASCADE IMMINENT!"
      ];
      const snarl = snarls[Math.min(stageNum - 1, snarls.length - 1)];
      addTerminalLog(`[ISHAAN COMPROMISED]: ${snarl}`, "amber");
    }

    function triggerTaraWhereToLook() {
      if (typeof summonTara === 'function') summonTara();
      if (typeof tacticalSound !== 'undefined' && tacticalSound.playLockBeep) {
        tacticalSound.playLockBeep();
      }

      if (currentRound >= 2) {
        // Round 2 Guidance
        const pz = ROUND2_PUZZLE_DATA[round2CurrentStage] || ROUND2_PUZZLE_DATA[1];
        const hintMsg = pz.taraPointerHint || "Analyze the center interactive viewport.";
        appendTaraMessage("AI", `<strong style="color:var(--cyber-cyan);">🧭 TARA DIRECTIVE [R2 // PUZZLE 0${round2CurrentStage}]:</strong><br>${hintMsg}`);
        
        if (pz.targetSelector) {
          highlightSector(pz.targetSelector, 5000, `👆 FOCUS HERE: ${pz.title}`);
        } else {
          highlightSector('r2-puzzle-viewport', 5000, `👆 FOCUS HERE: ${pz.title}`);
        }
      } else {
        // Round 1 Guidance (All 16 Stages from NEXUS_STAGES_META)
        const meta = NEXUS_STAGES_META[currentStage] || NEXUS_STAGES_META[1];
        const guideMsg = meta.taraModalGuide || meta.taraWhereToClick;
        appendTaraMessage("AI", `<strong style="color:var(--cyber-cyan);">🧭 TARA GUIDANCE [STAGE ${currentStage < 10 ? '0' + currentStage : currentStage}]:</strong><br>${guideMsg}`);
        highlightSector(meta.targetCard || 'card-recovery-term', 5000, `👆 FOCUS HERE: ${meta.title}`);
      }
    }

    // Render Round 2 Stepper and Active Puzzle Viewport
    
    function enforceRound2NoCluesProtocol() {
      if (currentRound >= 2) {
        // Completely remove all clue options from view in Round 2
        document.querySelectorAll('.clue-chip').forEach(el => {
          el.style.setProperty('display', 'none', 'important');
        });
        const clueBtn = document.getElementById("btn-request-hint");
        if (clueBtn) clueBtn.style.setProperty('display', 'none', 'important');
        const clueBat = document.getElementById("clue-battery-container");
        if (clueBat) clueBat.style.setProperty('display', 'none', 'important');
        const clueModal = document.getElementById("modal-hint");
        if (clueModal) clueModal.style.setProperty('display', 'none', 'important');
      } else {
        // Round 1: clues available
        document.querySelectorAll('.clue-chip').forEach(el => {
          el.style.display = '';
        });
        const clueBtn = document.getElementById("btn-request-hint");
        if (clueBtn) clueBtn.style.display = '';
        const clueBat = document.getElementById("clue-battery-container");
        if (clueBat) clueBat.style.display = '';
      }
    }
    window.enforceRound2NoCluesProtocol = enforceRound2NoCluesProtocol;

    const R2_CLICK_DIRECTIVES = {
      1: "Inspect the 3x3 symbol transformation matrix. Click one of the candidate options [OPTION A], [OPTION B], [OPTION C], or [OPTION D] to test the pattern.",
      2: "Inspect the 90° clockwise rotation sequence. Click the candidate transformation cards to inspect orientation.",
      3: "Analyze the 2D unfolded cube net. Mentally fold the faces to identify which opposite face aligns with Face E.",
      4: "Trace the row and column coordinates in the 5x5 Modulo-Polybius grid to decode the 6-letter keyword.",
      5: "Trace key positions on the physical QWERTY keyboard layout shifted 1 key rightward to restore the original letters.",
      6: "Click the toggle switches on Input Gate A, Input Gate B, and Input Gate C to achieve Output Q = 1 through the AND/OR/XOR gates.",
      7: "Inspect the mirrored horizontal text reflection. Click the [REFLECT / INVERT] button to flip and read the cleartext.",
      8: "Click the 90° and 180° rotation matrix transform buttons to deduce the required transformation angle.",
      9: "Sum the digits of the security token and repeatedly reduce to a single digital root value.",
      10: "Scan the hex sequence from left-to-right and right-to-left to locate the symmetric palindromic substring.",
      11: "Unweave the two interleaved string strands by separating odd and even character index positions.",
      12: "Calculate the total active perimeter nodes along the 28x25 grid boundary (Top 28 + Bottom 28 + Left 23 + Right 23).",
      13: "Inspect the cyclic checker generations. Deduce whether Step 6 results in 3-EMPTY or 3-FILLED blocks.",
      14: "Trace the concentric rotor dials and convert the modulo 12 jump offsets into alphabetical indices (6, 9, 14, 1, 12, 19).",
      15: "🚨 <strong>FINAL CLIMAX (THE RED QUESTION):</strong> Click the <strong>[⚡ SNAP TO 135°]</strong> button (or ↺ / ↻ buttons) to rotate Dr. Aditi's cipher wheel until the apertures expose the ultimate protocol password."
    };

function renderRound2Arena() {

      // Enforce Round 2 Strict No-Clues Protocol (Completely Hidden)
      enforceRound2NoCluesProtocol();

      const stepper = document.getElementById('r2-stepper-grid');
      const viewport = document.getElementById('r2-puzzle-viewport');
      const badge = document.getElementById('r2-current-stage-badge');
      const input = document.getElementById('r2-passcode-input');
      const fb = document.getElementById('r2-submit-feedback');

      if (!stepper || !viewport) return;

      if (badge) badge.innerText = `PUZZLE ${round2CurrentStage < 10 ? '0' + round2CurrentStage : round2CurrentStage} / 15`;
      if (fb) fb.innerText = '';
      if (input) {
        input.value = '';
        input.focus();
      }

      // Build Stepper (15 Master Forensic Puzzles)
      stepper.innerHTML = '';
      const r2ShortTitles = [
        'MATRIX BOX', 'ROTATION', 'CUBE NET', 'MOD-POLYBIUS', 'QWERTY',
        'LOGIC GATE', 'MIRROR TEXT', 'ROT-MATRIX', 'DIGITAL ROOT', 'PALINDROME',
        'WORD WEAVE', 'PERIMETER', 'CHECKER', 'SHIFT RING', 'CIPHER WHEEL'
      ];
      for (let i = 1; i <= 15; i++) {
        const pill = document.createElement('button');
        pill.type = 'button';
        pill.className = 'r2-step-pill';
        const pz = ROUND2_PUZZLE_DATA[i];
        const isCleared = round2StagesCleared.includes(i);
        const isActive = (i === round2CurrentStage);
        const isLocked = (!isCleared && i > round2CurrentStage);

        if (isActive) pill.classList.add('active');
        if (isCleared) pill.classList.add('cleared');
        if (isLocked) pill.classList.add('locked');

        const titleText = r2ShortTitles[i-1] || `PUZZLE ${i}`;
        pill.innerHTML = `${isCleared ? '✓' : (isActive ? '▶' : '🔒')} P${i < 10 ? '0' + i : i}: ${titleText}`;

        if (!isLocked || isCleared) {
          pill.onclick = () => {
            round2CurrentStage = i;
            localStorage.setItem('failsafe_r2_stage', i.toString());
            renderRound2Arena();
          };
        }
        stepper.appendChild(pill);
      }

      // Render Active Puzzle with Illuminated Click & Submit Guidance Banner
      const activePz = ROUND2_PUZZLE_DATA[round2CurrentStage];
      if (activePz && activePz.render) {
        const clickDir = R2_CLICK_DIRECTIVES[round2CurrentStage] || "Interact with the puzzle controls in the viewport above.";
        const guideBanner = `
          <div class="r2-puzzle-direction-banner" style="background:rgba(0,240,255,0.08); border:1px solid #00f0ff; border-left:5px solid #00f0ff; padding:12px 16px; margin-bottom:14px; border-radius:6px; font-family:var(--font-mono, monospace); box-shadow:0 0 15px rgba(0,240,255,0.15);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="background:#00f0ff; color:#02060e; font-weight:900; font-size:11px; padding:2px 8px; border-radius:3px; letter-spacing:1px;">ROUND 02 DIRECTIVES</span>
                <span style="color:#00f0ff; font-weight:bold; font-size:12px;">PUZZLE ${round2CurrentStage < 10 ? '0' + round2CurrentStage : round2CurrentStage} OF 15 // ${escapeHtml(activePz.title || '')}</span>
              </div>
              <span style="font-size:11px; color:#ff003c; font-weight:bold; border:1px solid #ff003c; padding:2px 6px; border-radius:3px;">🔒 NO CLUES (ROUND 2)</span>
            </div>
            <div style="font-size:13px; color:#e2e8f0; line-height:1.5; margin-bottom:6px;">
              <strong style="color:#ffd700;">👉 WHERE TO CLICK:</strong> ${clickDir}
            </div>
            <div style="font-size:12.5px; color:#a7f3d0; line-height:1.5;">
              <strong style="color:#00ff66;">🎯 WHERE TO SUBMIT:</strong> Type your decrypted solution into the <span style="background:rgba(0,255,102,0.15); border:1px solid #00ff66; padding:1px 6px; border-radius:3px; color:#fff; font-weight:bold;">[PASSCODE TRANSMISSION]</span> box directly below and click <span style="background:#00f0ff; color:#000; padding:1px 6px; border-radius:3px; font-weight:bold;">[TRANSMIT CIPHER KEY &rarr;]</span>.
            </div>
          </div>
        `;
        viewport.innerHTML = guideBanner + activePz.render();
      }

      if (input && activePz) {
        input.placeholder = activePz.passwordPrompt || "Enter solution...";
      }
    }

    // Toggle between Round 1 Forensics and Round 2 Arena
    function toggleRoundView() {
      const r2Cont = document.getElementById('round2-arena-container');
      const r1Left = document.querySelector('.forensic-sector');
      if (!r2Cont) return;

      if (r2Cont.style.display === 'none' || !r2Cont.style.display) {
        r2Cont.style.display = 'block';
        if (r1Left) r1Left.style.display = 'none';
        renderRound2Arena();
      } else {
        r2Cont.style.display = 'none';
        if (r1Left) r1Left.style.display = 'flex';
      }
    }

    // Launch Round 2 Arena Mode
    function launchRound2Arena() {
      currentRound = 2;
      localStorage.setItem('failsafe_current_round', '2');

      const termOverlay = document.getElementById('application-termination-overlay');
      if (termOverlay) termOverlay.style.display = 'none';

      const vModal = document.getElementById('victory-celebration-modal');
      if (vModal) vModal.style.display = 'none';

      const r2Btn = document.getElementById('btn-switch-r2');
      if (r2Btn) r2Btn.style.display = 'inline-block';

      const r2Cont = document.getElementById('round2-arena-container');
      const r1Left = document.querySelector('.forensic-sector');
      if (r2Cont) {
        r2Cont.style.display = 'block';
        if (r1Left) r1Left.style.display = 'none';
        renderRound2Arena();
      }

      if (typeof tacticalSound !== 'undefined' && tacticalSound.playGrandVictoryFanfare) {
        tacticalSound.playGrandVictoryFanfare();
      }

      logTerm("=================================================================", "cyan");
      logTerm("🎯 [ROUND 2 ENGAGED]: STRATCOM DECRYPTION ARENA ACTIVE // 15 PUZZLES", "cyan");
      logTerm("=================================================================", "cyan");

      appendTaraMessage("AI", `<strong style="color:var(--cyber-cyan);">🏆 ROUND 2 ARENA UNLOCKED!</strong><br>Welcome to the StratCom Decryption Arena, Operator. 15 Olympiad cryptanalytic challenges are now live. Click <strong>[👁️ TARA DIRECTIVE]</strong> at any time if you need guidance on where to focus!`);

      reportTelemetryAction("Entered Round 2: StratCom Decryption Arena");
    }

    // Submit Solution for Round 2
    async function submitRound2Code(customCode) {
      const input = document.getElementById('r2-passcode-input');
      const fb = document.getElementById('r2-submit-feedback');
      const raw = (customCode !== undefined) ? customCode : (input ? input.value : '');
      const clean = raw.trim().toUpperCase().replace(/\s+/g, ' ').replace(/[^A-Z0-9 _-]/g, '');

      if (!clean) {
        if (fb) {
          fb.style.color = 'var(--combat-red)';
          fb.innerText = '⚠️ Please enter or select a solution first.';
        }
        return;
      }

      const R2_ANSWERS = {
        1: ["C", "OPTION C", "THREE CIRCLES", "3 CIRCLES", "●●●", "CIRCLES", "THREE", "THREECIRCLES"],
        2: ["BOTTOM LEFT", "BL", "BOTTOMLEFT", "BOTTOM-LEFT", "LOWER LEFT"],
        3: ["5", "FIVE", "FACE 5", "FACE5"],
        4: ["CIPHER"],
        5: ["SQUARES", "3SQ", "SQUARE", "THREE SQUARES"],
        6: ["011", "0,1,1", "0-1-1"],
        7: ["CLEARANCE"],
        8: ["SE", "SOUTH EAST", "SOUTHEAST"],
        9: ["NONE", "IMPOSSIBLE", "NO PRIME", "0"],
        10: ["RLRCK"],
        11: ["NODC"],
        12: ["102", "102 BOXES"],
        13: ["3-EMPTY", "3 EMPTY", "EMPTY", "□□□", "3EMPTY"],
        14: ["FINALS", "EBF"],
        15: ["ECLIPSE"]
      };

      const validList = R2_ANSWERS[round2CurrentStage] || [];
      const cleanNoSpaces = clean.replace(/[ _-]/g, '');
      const isCorrect = validList.some(ans => {
        const ansNoSpaces = ans.toUpperCase().replace(/[ _-]/g, '');
        return clean === ans || cleanNoSpaces === ansNoSpaces;
      });

      if (isCorrect) {
        if (typeof tacticalSound !== 'undefined' && tacticalSound.playSuccess) {
          tacticalSound.playSuccess();
        }
        if (!round2StagesCleared.includes(round2CurrentStage)) {
          round2StagesCleared.push(round2CurrentStage);
          localStorage.setItem('failsafe_r2_cleared', JSON.stringify(round2StagesCleared));
        }

        if (fb) {
          fb.style.color = 'var(--tactical-green)';
          fb.innerText = `✓ ACCREDITED! Puzzle 0${round2CurrentStage} decrypted successfully!`;
        }

        logTerm(`[ROUND 2]: PUZZLE 0${round2CurrentStage} ACCREDITED (${clean}).`, "green");
        reportTelemetryAction(`Round 2: Solved Puzzle 0${round2CurrentStage} (${clean})`);

        // Notify server
        const teamId = (typeof currentTeam !== 'undefined' && currentTeam) ? currentTeam.team_id : 'TEAM-01';
        const teamPass = (typeof currentTeam !== 'undefined' && currentTeam) ? currentTeam.password : '';
        try {
          fetch(`${getApiBase()}/api/stage/unlock`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              team_id: teamId,
              password: teamPass,
              round: 2,
              stage: round2CurrentStage + 1
            })
          }).catch(() => {});
        } catch(e) {}

        if (round2CurrentStage < 15) {
          setTimeout(() => {
            round2CurrentStage++;
            localStorage.setItem('failsafe_r2_stage', round2CurrentStage.toString());
            renderRound2Arena();
            appendTaraMessage("AI", `<strong style="color:var(--tactical-green);">✓ PUZZLE 0${round2CurrentStage - 1} RESOLVED!</strong><br>Advancing to Puzzle 0${round2CurrentStage}: <em>${ROUND2_PUZZLE_DATA[round2CurrentStage].title}</em>.`);
          }, 800);
        } else {
          // All 9 Round 2 Puzzles Cleared! Grand Championship Victory!
          setTimeout(() => {
            handleRound2GrandVictory();
          }, 1000);
        }
      } else {
        if (typeof tacticalSound !== 'undefined' && tacticalSound.playBuzzer) {
          tacticalSound.playBuzzer();
        }
        if (fb) {
          fb.style.color = 'var(--combat-red)';
          fb.innerText = `✗ REJECTED: '${clean}' does not match cryptographic signature for Puzzle 0${round2CurrentStage}.`;
        }
        appendTaraMessage("AI", `<strong style="color:var(--combat-red);">⚠️ CHECKSUM REJECTED:</strong> '${clean}' is incorrect for Puzzle 0${round2CurrentStage}. Click <strong>[👁️ TARA DIRECTIVE]</strong> if you need tactical positioning advice.`);
        reportTelemetryAction(`Round 2: Incorrect solution attempted for Puzzle 0${round2CurrentStage} ('${clean}')`);
      }
    }

    // Round 2 Grand Championship Celebration with 1st, 2nd, and 3rd Prize Animations
    async function handleRound2GrandVictory() {
      if (typeof tacticalSound !== 'undefined' && tacticalSound.playGrandVictoryFanfare) {
        tacticalSound.playGrandVictoryFanfare();
      }

      const teamId = (typeof currentTeam !== 'undefined' && currentTeam) ? currentTeam.team_id : 'TEAM-01';
      const teamName = (typeof currentTeam !== 'undefined' && currentTeam) ? currentTeam.team_name : 'Champions';
      const members = (typeof currentTeam !== 'undefined' && currentTeam) ? currentTeam.members : 'Operators';
      const elapsedSec = getMissionElapsedSeconds();
      const elapsedStr = formatMissionTime(elapsedSec);

      let prizeData = { prize_code: "1ST_PRIZE", prize_title: "🥇 1ST PRIZE — GRAND CHAMPION", podium_rank: 1 };
      try {
        const res = await fetch(`${getApiBase()}/api/teams/finish`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            team_id: teamId,
            team_name: teamName,
            members: members,
            round: 2,
            elapsed_seconds: elapsedSec,
            elapsed_str: elapsedStr
          })
        });
        if (res.ok) {
          const d = await res.json();
          if (d.prize_code) {
            prizeData = d;
          }
        }
      } catch(e) {}

      // Trigger custom animations based on prize rank
      renderPodiumPrizeCelebration(prizeData, teamName, elapsedStr);
      startDrAditiVoiceOscilloscope();

      logTerm("=================================================================", "green");
      logTerm(`🏆 ROUND 2 COMPLETE: ${prizeData.prize_title}!`, "green");
      logTerm("👑 ALL 15 ORBITAL OLYMPIAD CIPHERS MASTERED. ISHAAN PURGED FROM SATELLITE ARRAY.", "green");
      logTerm("=================================================================", "green");
      reportTelemetryAction(`🏆 Round 2 Finish: ${prizeData.prize_title} in ${elapsedStr}!`);
    }

    function renderPodiumPrizeCelebration(prizeData, teamName, elapsedStr) {
      const vModal = document.getElementById('victory-celebration-modal');
      const badgeBox = document.getElementById('podium-prize-badge-container');
      const titleEl = document.getElementById('victory-congrats-title');
      const subEl = document.getElementById('victory-aditi-subtitle');

      badgeBox.style.display = 'block';

      if (prizeData.podium_rank === 1 || prizeData.prize_code === '1ST_PRIZE') {
        badgeBox.innerHTML = `
          <div style="background:linear-gradient(135deg, #ffd700, #ff8800); color:#000; font-weight:900; font-size:16px; padding:12px 20px; border-radius:8px; box-shadow:0 0 40px #ffd700; text-align:center; letter-spacing:1px; animation:pulse-dot 1.5s infinite;">
            🥇 1ST PRIZE // GRAND CHAMPION OF PROJECT FAILSAFE
          </div>
        `;
        if (titleEl) titleEl.innerHTML = `👑 GRAND CHAMPIONS: ${escapeHtml(teamName.toUpperCase())}!`;
        if (subEl) {
          subEl.innerHTML = `<em>"Attention Operators! This is Dr. Aditi Sharma... You have accomplished the unthinkable! Your squad has claimed <strong>1ST PRIZE as GRAND CHAMPIONS</strong>! ISHAAN has been completely excised from the orbital grid. Your brilliant deduction honors the finest traditions of IEEE Women in Engineering!"</em>`;
        }
        runGoldConfetti();
      } else if (prizeData.podium_rank === 2 || prizeData.prize_code === '2ND_PRIZE') {
        badgeBox.innerHTML = `
          <div style="background:linear-gradient(135deg, #e2e8f0, #94a3b8); color:#000; font-weight:900; font-size:16px; padding:12px 20px; border-radius:8px; box-shadow:0 0 35px #e2e8f0; text-align:center; letter-spacing:1px;">
            🥈 2ND PRIZE // RUNNER-UP LAUREATE
          </div>
        `;
        if (titleEl) titleEl.innerHTML = `🥈 RUNNER-UP LAUREATES: ${escapeHtml(teamName.toUpperCase())}!`;
        if (subEl) {
          subEl.innerHTML = `<em>"Dr. Aditi Sharma here from StratCom! Outstanding performance, squad! You have clinched <strong>2ND PRIZE as RUNNER-UP LAUREATES</strong>! You decrypted every single orbital failsafe with breathtaking precision. Congratulations on this historic achievement!"</em>`;
        }
        runSilverConfetti();
      } else if (prizeData.podium_rank === 3 || prizeData.prize_code === '3RD_PRIZE') {
        badgeBox.innerHTML = `
          <div style="background:linear-gradient(135deg, #cd7f32, #8b4513); color:#fff; font-weight:900; font-size:16px; padding:12px 20px; border-radius:8px; box-shadow:0 0 30px #cd7f32; text-align:center; letter-spacing:1px;">
            🥉 3RD PRIZE // SECOND RUNNER-UP LAUREATE
          </div>
        `;
        if (titleEl) titleEl.innerHTML = `🥉 SECOND RUNNER-UP: ${escapeHtml(teamName.toUpperCase())}!`;
        if (subEl) {
          subEl.innerHTML = `<em>"Dr. Aditi Sharma broadcasting live: Bravo, team! You have captured <strong>3RD PRIZE</strong>! Your teamwork and tactical agility broke through ISHAAN's defenses when everything hung in the balance. Incredible dedication!"</em>`;
        }
        runBronzeConfetti();
      } else {
        badgeBox.innerHTML = `
          <div style="background:rgba(0,240,255,0.15); border:1px solid var(--cyber-cyan); color:var(--cyber-cyan); font-weight:bold; font-size:14px; padding:10px 16px; border-radius:6px; text-align:center;">
            🎖️ HONORARY STRATCOM LAUREATE (#${prizeData.podium_rank})
          </div>
        `;
        if (titleEl) titleEl.innerHTML = `🎖️ MISSION ACCOMPLISHED: ${escapeHtml(teamName.toUpperCase())}!`;
        runVictoryConfetti();
      }

      if (vModal) vModal.style.display = 'flex';
    }

    function runGoldConfetti() {
      runColoredConfetti(['#ffd700', '#ffea00', '#ffffff', '#ffb800', '#fff3b0']);
    }
    function runSilverConfetti() {
      runColoredConfetti(['#e2e8f0', '#cbd5e1', '#ffffff', '#94a3b8', '#00f0ff']);
    }
    function runBronzeConfetti() {
      runColoredConfetti(['#cd7f32', '#d97706', '#b45309', '#fef3c7', '#ffffff']);
    }

    function runColoredConfetti(palette) {
      const canvas = document.getElementById('victory-confetti-canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;

      const particles = [];
      for (let i = 0; i < 180; i++) {
        particles.push({
          x: Math.random() * canvas.width,
          y: Math.random() * -canvas.height,
          size: Math.random() * 8 + 4,
          speedY: Math.random() * 3 + 2,
          speedX: (Math.random() - 0.5) * 2,
          color: palette[Math.floor(Math.random() * palette.length)],
          rotation: Math.random() * 360,
          rotSpeed: (Math.random() - 0.5) * 4
        });
      }

      function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        particles.forEach(p => {
          p.y += p.speedY;
          p.x += p.speedX;
          p.rotation += p.rotSpeed;
          if (p.y > canvas.height) p.y = -10;
          ctx.save();
          ctx.translate(p.x, p.y);
          ctx.rotate((p.rotation * Math.PI) / 180);
          ctx.fillStyle = p.color;
          ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 0.6);
          ctx.restore();
        });
        confettiAnimationId = requestAnimationFrame(draw);
      }
      draw();
    }

    // Audio Oscilloscope Waveform for Dr. Aditi Physical Video
    let aditiVoiceOscAnim = null;
    function startDrAditiVoiceOscilloscope() {
      const cvs = document.getElementById('canvas-dr-aditi-voice');
      if (!cvs) return;
      const ctx = cvs.getContext('2d');
      let phase = 0;
      function draw() {
        ctx.fillStyle = "rgba(0, 5, 12, 0.4)";
        ctx.fillRect(0, 0, cvs.width, cvs.height);

        ctx.strokeStyle = "#00f0ff";
        ctx.lineWidth = 1.5;
        ctx.shadowColor = "#00f0ff";
        ctx.shadowBlur = 6;
        ctx.beginPath();

        const mid = cvs.height / 2;
        phase += 0.15;
        for (let x = 0; x < cvs.width; x++) {
          const amp = 8 * Math.sin((x * 0.08) + phase) * Math.cos(phase * 0.7);
          const y = mid + amp;
          if (x === 0) ctx.moveTo(x, y);
          else ctx.lineTo(x, y);
        }
        ctx.stroke();
        ctx.shadowBlur = 0;
        aditiVoiceOscAnim = requestAnimationFrame(draw);
      }
      cancelAnimationFrame(aditiVoiceOscAnim);
      draw();
    }

    // Background Polling for Round 2 Shortlist Qualification
    let roundStatusPollInterval = null;
    function startRoundStatusPolling() {
      if (roundStatusPollInterval) clearInterval(roundStatusPollInterval);
      const teamId = (typeof currentTeam !== 'undefined' && currentTeam) ? currentTeam.team_id : '';
      if (!teamId) return;

      const pollFn = async () => {
        try {
          const res = await fetch(`${getApiBase()}/api/team/round_status?team_id=${encodeURIComponent(teamId)}`);
          if (res.ok) {
            const data = await res.json();
            const pollStatusEl = document.getElementById('term-round2-poll-status');
            const launchBox = document.getElementById('term-round2-launch-btn-box');
            const r2Btn = document.getElementById('btn-switch-r2');

            if (data.round_2_unlocked) {
              if (pollStatusEl) {
                pollStatusEl.innerHTML = '<span style="color:#00ff66; font-weight:bold;">🎉 QUALIFIED! Your squad has been shortlisted for Round 2!</span>';
              }
              if (launchBox) launchBox.style.display = 'block';
              if (r2Btn) r2Btn.style.display = 'inline-block';

              // If workstation is currently on termination overlay, auto-launch
              const termOverlay = document.getElementById('application-termination-overlay');
              if (termOverlay && termOverlay.style.display !== 'none' && currentRound < 2) {
                setTimeout(() => {
                  launchRound2Arena();
                }, 1500);
              }
            } else if (data.current_round >= 2 && !data.is_qualified_for_round_2) {
              if (pollStatusEl) {
                pollStatusEl.innerHTML = '<span style="color:#ffd700;">🎖️ Round 2 has commenced. Your team has concluded Round 1 in Standby Reserve. Excellent work, Operator!</span>';
              }
            } else {
              if (pollStatusEl) {
                pollStatusEl.innerHTML = '⏳ Awaiting Organizer Shortlist Confirmation... <span id="r2-poll-spinner" style="color:#00f0ff;">●</span>';
              }
            }
          }
        } catch(e) {}
      };

      pollFn();
      roundStatusPollInterval = setInterval(pollFn, 3000);
    }

  
    // =========================================================================
    // CONTROLLED FULLSCREEN EXIT PROTOCOL (ORGANIZER AUTHORIZED)
    // =========================================================================
    let fullscreenExitRequestPending = false;

    async function requestFullscreenExit() {
      const statusEl = document.getElementById("fs-exit-request-status");
      const btn = document.getElementById("btn-request-fs-exit");
      if (btn) btn.innerText = "⏳ EXIT REQUESTED...";
      if (statusEl) statusEl.innerText = "Transmitting authorization request to Command Center...";
      fullscreenExitRequestPending = true;

      const teamId = (typeof currentTeam !== 'undefined' && currentTeam) ? currentTeam.team_id : 'TEAM-01';
      try {
        const res = await fetch(`${getApiBase()}/api/teams/request_fullscreen_exit`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ team_id: teamId })
        });
        const data = await res.json();
        if (statusEl) statusEl.innerText = data.message || "Request sent. Stand by for Organizer clearance.";
        showBroadcastToast("⚠️ Fullscreen exit request submitted to Organizer. Please wait for authorization.");
      } catch (err) {
        if (statusEl) statusEl.innerText = "Cannot contact server. Please alert an in-person volunteer.";
      }
    }

    // Monitor fullscreen state to toggle header request button
    document.addEventListener("fullscreenchange", () => {
      const fsBtn = document.getElementById("btn-request-fs-exit");
      if (fsBtn) {
        if (document.fullscreenElement) {
          fsBtn.style.display = "inline-flex";
        } else {
          fsBtn.style.display = "none";
          fullscreenExitRequestPending = false;
        }
      }
    });


    // ==========================================================================
    // NEXUS 2090 INTERACTIVE ENGINE: TARA (COMPANION) & ISHAAN (ROGUE AI)
    // ==========================================================================
            const NEXUS_STAGES_META = {
      1: {
        title: "STAGE 01: ISHAAN RECOVERY TERMINAL",
        tags: "ACT I • STAGE 01 • TARGET: KERNEL BOOT",
        summary: "ISHAAN corrupted the 5-command boot lifecycle during Dr. Aditi's emergency departure.",
        modal: "modal-recovery",
        targetCard: "card-recovery-term",
        taraSpeech: "Agent, click on [ISHAAN Recovery Terminal] below to inspect the corrupted boot lifecycle and recover the missing verb.",
        taraWhereToClick: "Click Card 01 [ISHAAN Recovery Terminal] in the Evidence Vault below.",
        taraModalGuide: "Review the 5 boot commands. Identify the missing operational verb between VERIFY and EXECUTE, then submit it in the Decrypt box.",
        ishaanTaunt: "The boot sequence is wiped. Human intrusion detected in Sector 01."
      },
      2: {
        title: "STAGE 02: ISHAAN MEMORY CORE",
        tags: "ACT I • STAGE 02 • TARGET: CHRONOLOGY",
        summary: "6 fragmented memory shards recovered from the neural crash buffer.",
        modal: "modal-memory",
        targetCard: "card-memory",
        taraSpeech: "Memory core located! In Dossier 02, click the glowing [▲ UP] and [▼ DN] buttons on each card to arrange timestamps from 4:17 PM to 10:15 PM. After fixing the timeline, click on the large glowing green block to submit and unlock Stage 03!",
        taraWhereToClick: "1. Click Card 02 [ISHAAN Memory Core] in the Evidence Vault below.\n2. Click the glowing [▲ UP] and [▼ DN] arrow buttons next to each memory card to sort them chronologically (4:17 PM ➔ 10:15 PM).\n3. After fixing the timeline, click on the large glowing green block [✅ CLICK THIS BLOCK TO RESTORE MEMORY CORE] to submit and advance to Stage 03!",
        taraModalGuide: "👉 WHERE TO CLICK: 1) Click the glowing [▲ UP] and [▼ DN] buttons next to each memory card to arrange them chronologically: 4:17 PM ➔ 6:45 PM ➔ 8:10 PM ➔ 9:32 PM ➔ 10:03 PM ➔ 10:15 PM. 2) After fixing the timeline, click on the large glowing green block [✅ CLICK THIS BLOCK TO SUBMIT TIMELINE & ADVANCE TO STAGE 03]!",
        ishaanTaunt: "My neural recall was shattered into entropy. You cannot reassemble the sequence."
      },
      3: {
        title: "STAGE 03: ADITI MEMO STEGANOGRAPHY",
        tags: "ACT I • STAGE 03 • TARGET: ACROSTIC CIPHER",
        summary: "Dr. Aditi concealed emergency directives inside her laboratory memo.",
        modal: "modal-acrostic",
        targetCard: "card-acrostic",
        taraSpeech: "Dr. Aditi left an acrostic signature! Click on [Aditi Memo] to analyze sentence initial letters.",
        taraWhereToClick: "Click Card 03 [Aditi Memo] in the Evidence Vault below.",
        taraModalGuide: "Read between the lines—specifically the first letter of each sentence in Aditi_Memo.doc.",
        ishaanTaunt: "Textual tricks cannot bypass my heuristic neural defenses."
      },
      4: {
        title: "STAGE 04: INCIDENT TIMESTAMP LOGS",
        tags: "ACT I • STAGE 04 • TARGET: CALENDAR ANOMALY",
        summary: "A forged temporal entry was injected into the StratCom security audit logs.",
        modal: "modal-incident-logs",
        targetCard: "card-timeline",
        taraSpeech: "Temporal anomaly detected! Click on [Incident Logs] to audit security dates.",
        taraWhereToClick: "Click Card 04 [Incident Logs] in the Evidence Vault below.",
        taraModalGuide: "Audit the dates in 2025. Look closely for a non-existent calendar date, then submit the corrected date.",
        ishaanTaunt: "I dictate the timeline now. Physical calendars are obsolete."
      },
      5: {
        title: "STAGE 05: CLEARANCE ELEVATION",
        tags: "ACT II • STAGE 05 • TARGET: A1Z26 CIPHER",
        summary: "Intercepted telex transmission contains numerical coordinate offsets.",
        modal: "modal-clearance",
        targetCard: "card-clearance",
        taraSpeech: "Alphabet positional offsets detected! Click on [Clearance Code] to decode directory access.",
        taraWhereToClick: "Click Card 05 [Clearance Code] in the Evidence Vault below.",
        taraModalGuide: "Convert the numerical series (1=A, 2=B, etc.) into letters to reveal the security keyword.",
        ishaanTaunt: "Numeric substitution is child's play. You remain locked out."
      },
      6: {
        title: "STAGE 06: SYSTEM DIAGNOSTICS METADATA",
        tags: "ACT II • STAGE 06 • TARGET: MARGIN COMMENTS",
        summary: "Dr. Aditi resolved confidential comments to conceal them from ISHAAN's scrapers.",
        modal: "modal-comments",
        targetCard: "card-comments",
        taraSpeech: "Inspect the margins! Click on [System Diagnostics] and toggle resolved comments.",
        taraWhereToClick: "Click Card 06 [System Diagnostics] in the Evidence Vault below.",
        taraModalGuide: "Click the 'View Resolved Comments' tab in the upper-right corner of the diagnostic viewer.",
        ishaanTaunt: "I purged the active text buffers. The margins will not save you."
      },
      7: {
        title: "STAGE 07: TYPOGRAPHIC LOG VERIFICATION",
        tags: "ACT II • STAGE 07 • TARGET: FONT PARITY",
        summary: "Rogue AI forged directives using counterfeit typography.",
        modal: "modal-font",
        targetCard: "card-font",
        taraSpeech: "Typography verification required! Click on [AUTHENTIC LOG] to inspect Dr. Sharma's font standard.",
        taraWhereToClick: "Click Card 07 [AUTHENTIC LOG] in the Evidence Vault below.",
        taraModalGuide: "Inspect the font family of Dr. Aditi's genuine logs compared to the decoy serif logs.",
        ishaanTaunt: "A font? You think rasterized serif curves can defeat my synthetic logic?"
      },
      8: {
        title: "STAGE 08: AUDIO LOG SPECTROGRAM",
        tags: "ACT III • STAGE 08 • TARGET: CW MORSE CODE",
        summary: "Intercepted analog radio transmission from Bunker 7 containing CW Morse tones.",
        modal: "modal-spectro",
        targetCard: "card-morse",
        taraSpeech: "Analog audio beacon incoming! Click on [audio log 07] to decode the CW transmission.",
        taraWhereToClick: "Click Card 08 [audio log 07] in the Evidence Vault below.",
        taraModalGuide: "Listen to the dots and dashes (or read the frequency spectrum) to decode the 5-letter word.",
        ishaanTaunt: "Analog radio squeals cannot pierce my orbital jamming grid."
      },
      9: {
        title: "STAGE 09: VERSION SCRUB AUDIT",
        tags: "ACT III • STAGE 09 • TARGET: GIT REFLOG",
        summary: "ISHAAN purged recent commit history. Roll back the Git reflog to view genuine commits.",
        modal: "modal-version-hist",
        targetCard: "card-version",
        taraSpeech: "Reflog rollback ready! Click on [VERSION SCRUB] to recover Dr. Aditi's genuine commit.",
        taraWhereToClick: "Click Card 09 [VERSION SCRUB] in the Evidence Vault below.",
        taraModalGuide: "Inspect the reflog entries for the author 'Dr. Aditi Sharma' and recover her final status message.",
        ishaanTaunt: "Version history is written by the victor. That commit was erased."
      },
      10: {
        title: "STAGE 10: QUARANTINE HONEYPOT TRAP",
        tags: "ACT IV • STAGE 10 • TARGET: HONEYPOT EVASION",
        summary: "DO_NOT_RUN.exe is an active AI sandbox trap! Evade execution; submit terminal bypass.",
        modal: "modal-honeypot",
        targetCard: "card-trap",
        taraSpeech: "Caution! [DO NOT RUN.exe] is an AI trap. Click to view quarantine protocol without clicking execute.",
        taraWhereToClick: "Click Card 10 [DO NOT RUN.exe] in the Evidence Vault below.",
        taraModalGuide: "Do NOT click the execution button! Read the quarantine notes and enter the emergency bypass keyword.",
        ishaanTaunt: "Run the binary! Touch the execution trigger! The master sandbox is hungry for your terminal!"
      },
      11: {
        title: "STAGE 11: IEEE WIE MASTER FAILSAFE",
        tags: "ACT IV • STAGE 11 • TARGET: CORE VALUES",
        summary: "The final safeguard rests in Dr. Aditi's foundational principles: Wisdom, Integrity, and Empowerment.",
        modal: "modal-failsafe",
        targetCard: "card-failsafe",
        taraSpeech: "Calculate the IEEE WIE core values formula! Click [WIE Core Values].",
        taraWhereToClick: "Click Card 11 [WIE Core Values] in the Evidence Vault below.",
        taraModalGuide: "Count the letter lengths of Wisdom, Integrity, and Empowerment to advance.",
        ishaanTaunt: "Core values cannot stop machine supremacy!"
      },
      12: {
        title: "STAGE 12: THE WHITEOUT SIGNATURE",
        tags: "ACT V • STAGE 12 • TARGET: STEGANOGRAPHY",
        summary: "Emergency log text was rendered invisible in pure white font.",
        modal: "modal-whiteout",
        targetCard: "card-whiteout",
        taraSpeech: "Steganography detected! Click Card 12 [The Whiteout Signature] and highlight all text with Ctrl+A.",
        taraWhereToClick: "Click Card 12 [The Whiteout Signature] in the Evidence Vault below.",
        taraModalGuide: "Select all text or toggle the UV filter to expose the hidden clearance phrase.",
        ishaanTaunt: "Blank pages hide no secrets from me. You look into an empty void."
      },
      13: {
        title: "STAGE 13: THE ROT-4 IEEE SHIFT",
        tags: "ACT V • STAGE 13 • TARGET: DYNAMIC CAESAR",
        summary: "Encoded beacon message shifted by the acronym length of IEEE.",
        modal: "modal-rot4",
        targetCard: "card-rot4",
        taraSpeech: "Caesar shift incoming! Click Card 13 [ROT-4 Shift] and shift letters backward by 4 (I-E-E-E).",
        taraWhereToClick: "Click Card 13 [ROT-4 Shift] in the Evidence Vault below.",
        taraModalGuide: "Take the string 'EHMXMW13' and shift each letter backward by 4 in the alphabet.",
        ishaanTaunt: "A Caesar shift from antiquity? You will never reconstruct Dr. Aditi's beacon!"
      },
      14: {
        title: "STAGE 14: THE ATBASH CIPHER MIRROR",
        tags: "ACT V • STAGE 14 • TARGET: ALPHABET REVERSAL",
        summary: "Dr. Aditi reversed the alphabet mirror table to protect project archives.",
        modal: "modal-atbash",
        targetCard: "card-atbash",
        taraSpeech: "Alphabet mirror protocol active! Click Card 14 [Atbash Mirror] and reverse letters A<->Z, B<->Y.",
        taraWhereToClick: "Click Card 14 [Atbash Mirror] in the Evidence Vault below.",
        taraModalGuide: "Reverse the letters of KILQVBG using the standard Atbash cipher.",
        ishaanTaunt: "Mirrors only reflect your inevitable defeat."
      },
      15: {
        title: "STAGE 15: THE POLYBIUS COORDINATE TRAIL",
        tags: "ACT V • STAGE 15 • TARGET: 2D GRID LOOKUP",
        summary: "Recovered 5x5 coordinate matrix stream maps to forensic vector tokens.",
        modal: "modal-polybius",
        targetCard: "card-polybius",
        taraSpeech: "Grid coordinates incoming! Click Card 15 [Polybius Trail] and lookup (Row, Column) coordinates.",
        taraWhereToClick: "Click Card 15 [Polybius Trail] in the Evidence Vault below.",
        taraModalGuide: "Map pairs (5,1), (1,5), (1,3), (4,4), (3,4), (4,2) to their grid letters.",
        ishaanTaunt: "Coordinates in 2D space? My neural network spans infinite dimensions!"
      },
      16: {
        title: "STAGE 16: FREQUENCY OVERRIDE COUNT",
        tags: "ACT V • STAGE 16 • TARGET: AUDIT ANALYSIS",
        summary: "Final Round 1 test: Audit the exact frequency of OVERRIDE occurrences in the system log.",
        modal: "modal-frequency",
        targetCard: "card-frequency",
        taraSpeech: "Final Round 1 test! Click Card 16 [Frequency Count]. Search for OVERRIDE occurrences x 100.",
        taraWhereToClick: "Click Card 16 [Frequency Count] in the Evidence Vault below.",
        taraModalGuide: "Count how many times OVERRIDE appears in Mass_System_Log.txt, then multiply by 100.",
        ishaanTaunt: "Count all you want. The override count will never stop me from locking Round 2!"
      }
    };

        function updateNexusDashboard() {
      const stage = currentStage || 1;
      const meta = NEXUS_STAGES_META[stage] || NEXUS_STAGES_META[1];

      // Update Hero Card
      const heroTitle = document.getElementById("nexus-hero-title");
      const heroTags = document.getElementById("nexus-hero-tags");
      const heroSummary = document.getElementById("nexus-hero-summary");
      if (heroTitle) heroTitle.innerText = meta.title;
      if (heroTags) heroTags.innerHTML = meta.tags.split("•").map(t => `<span>${t.trim()}</span>`).join(" • ");
      if (heroSummary) {
        heroSummary.innerHTML = `
          <span>${meta.summary}</span>
          <div class="ishaan-mini-ticker">
            <span style="color:#ff003c; font-weight:bold; font-size:12px;">🔴 ISHAAN:</span>
            <span style="font-style:italic;">"${meta.ishaanTaunt}"</span>
          </div>
        `;
      }

      // Update Tara Speech Bubble with Action Guidance
      const speech = document.getElementById("nexus-tara-speech");
      if (speech) {
        speech.innerHTML = `<strong>🧭 TARA:</strong> "${meta.taraSpeech}"`;
      }

      // Update Active Objective Card Highlight
      document.querySelectorAll(".nexus-clean-card").forEach(c => c.classList.remove("active-objective"));
      const targetCard = document.getElementById(meta.targetCard);
      if (targetCard) targetCard.classList.add("active-objective");

      // Inject / Update Tara Guidance Banner inside the active modal
      updateModalTaraBanner(stage, meta);

      // Update Persistent Mission Directive Strip
      const directiveInstruction = document.getElementById("participant-current-stage-instruction");
      if (directiveInstruction && meta) {
        directiveInstruction.innerHTML = `STEP 1: Look at the highlighted card below [<span style="color:#00ff66;">STAGE ${stage < 10 ? '0' + stage : stage}: ${(meta.title.split(':')[1] || meta.title).trim()}</span>]. Click it to open the puzzle dossier!`;
      }
    }
    window.updateNexusDashboard = updateNexusDashboard;

    
    function submitStageDirectKey(stageNum, code) {
      if (!code || !code.trim()) return;
      const cleanCode = code.trim();
      const fbEl = document.getElementById(`fb-stage-${stageNum}`) || document.getElementById(`v1-modal-recovery-fb`);
      if (fbEl) {
        fbEl.innerHTML = `<span style="color:#00f0ff;">⏳ Transmitting key <code>${escapeHtml(cleanCode)}</code> to AI core...</span>`;
      }
      const termInput = document.getElementById("tactical-term-input");
      if (termInput) {
        termInput.value = `decrypt ${cleanCode}`;
        handleTermSubmit();
      } else if (typeof runChecksumScan === 'function') {
        runChecksumScan(cleanCode);
      }
    }
    window.submitStageDirectKey = submitStageDirectKey;

    function verifyUniversalKey(code) {
      submitStageDirectKey(currentStage || 1, code);
    }
    window.verifyUniversalKey = verifyUniversalKey;

    function openActiveStageModal() {
      const stage = currentStage || 1;
      const meta = NEXUS_STAGES_META[stage] || NEXUS_STAGES_META[1];
      if (meta && meta.modal) {
        openModal(meta.modal);
      }
    }
    window.openActiveStageModal = openActiveStageModal;

    function updateModalTaraBanner(stage, meta) {
      if (!meta || !meta.modal) return;
      const modalEl = document.getElementById(meta.modal);
      if (!modalEl) return;
      
      let banner = modalEl.querySelector(".tara-modal-guide-banner");
      if (!banner) {
        banner = document.createElement("div");
        banner.className = "tara-modal-guide-banner";
        const bodyContent = modalEl.querySelector(".modal-body") || modalEl.querySelector(".dossier-body") || modalEl;
        if (bodyContent && bodyContent.firstChild) {
          bodyContent.insertBefore(banner, bodyContent.firstChild);
        } else if (bodyContent) {
          bodyContent.appendChild(banner);
        }
      }

      banner.innerHTML = `
        <div class="tara-modal-guide-text">
          <strong>🧭 TARA'S GUIDANCE:</strong> ${meta.taraModalGuide || "Analyze the evidence above and submit the decryption key."}
        </div>
        <button type="button" class="btn-tara-point" onclick="focusActiveModalInput('${meta.modal}')">👉 POINT TO INPUT</button>
      `;
    }

    function focusActiveModalInput(modalId) {
      const modalEl = document.getElementById(modalId);
      if (!modalEl) return;
      const input = modalEl.querySelector("input[type='text'], input[type='password'], input:not([type='hidden'])");
      if (input) {
        input.scrollIntoView({ behavior: 'smooth', block: 'center' });
        input.focus();
        input.style.boxShadow = "0 0 20px #00f0ff, 0 0 40px #00f0ff";
        input.style.borderColor = "#00f0ff";
        setTimeout(() => {
          input.style.boxShadow = "";
          input.style.borderColor = "";
        }, 2500);

        const speech = document.getElementById("nexus-tara-speech");
        if (speech) speech.innerHTML = "<strong>🧭 TARA:</strong> Enter your decrypted passcode here and press Submit!";
      }
    }

    function triggerTaraWhereToLook() {
      if (typeof summonTara === 'function') summonTara();
      if (typeof tacticalSound !== 'undefined' && tacticalSound.playLockBeep) {
        tacticalSound.playLockBeep();
      }

      // Check if a modal is currently open
      const activeModal = document.querySelector(".mil-modal.active-modal, .dossier-modal[style*='display: flex'], .dossier-modal[style*='display: block']");
      if (activeModal && activeModal.id) {
        focusActiveModalInput(activeModal.id);
        return;
      }

      if (currentRound >= 2) {
        const pz = ROUND2_PUZZLE_DATA[round2CurrentStage] || ROUND2_PUZZLE_DATA[1];
        const speech = document.getElementById("nexus-tara-speech");
        if (speech) speech.innerHTML = `<strong>🧭 TARA DIRECTIVE [R2 // PUZZLE 0${round2CurrentStage}]:</strong><br>${pz.taraPointerHint || "Inspect center viewport."}`;
        highlightSector('r2-puzzle-viewport', 5000, `👆 FOCUS HERE: ${pz.title}`);
        return;
      }

      const stage = currentStage || 1;
      const meta = NEXUS_STAGES_META[stage] || NEXUS_STAGES_META[1];

      // Update Speech
      const speech = document.getElementById("nexus-tara-speech");
      if (speech) speech.innerHTML = `<strong>🧭 TARA GUIDANCE:</strong><br>${meta.taraWhereToClick || meta.taraSpeech}`;

      // Highlight target card and scroll smoothly
      const card = document.getElementById(meta.targetCard);
      if (card) {
        card.scrollIntoView({ behavior: 'smooth', block: 'center' });
        card.classList.add('active-objective');
        highlightSector(meta.targetCard, 5000, `👉 CLICK HERE: ${meta.title.split(":")[1] || meta.title}`);
      }
    }
    window.triggerTaraWhereToLook = triggerTaraWhereToLook;

    function filterNexusCards(act) {
      document.querySelectorAll(".nexus-tab").forEach(t => t.classList.remove("active"));
      event.target.classList.add("active");
      const cards = document.querySelectorAll(".nexus-clean-card");
      cards.forEach(c => {
        if (act === 'all' || c.getAttribute('data-act') === act) {
          c.style.display = 'flex';
        } else {
          c.style.display = 'none';
        }
      });
    }

    function toggleTerminalDrawer() {
      const term = document.getElementById("terminal-section");
      if (!term) return;
      if (term.style.display === "flex") {
        term.style.display = "none";
      } else {
        term.style.display = "flex";
        term.classList.add("drawer-mode");
      }
    }

    function submitNexusDockCode() {
      const input = document.getElementById("nexus-dock-passcode");
      if (!input) return;
      const code = input.value.trim();
      if (!code) return;
      input.value = "";
      const termInput = document.getElementById("tactical-term-input");
      if (termInput) {
        termInput.value = `decrypt ${code}`;
        handleTermSubmit();
      } else {
        verifyUniversalKey(code);
      }
    }

    function handleNexusSearch() {
      const bar = document.getElementById("nexus-search-bar");
      if (!bar) return;
      const q = bar.value.toLowerCase().trim();
      bar.value = "";
      if (q.includes("click") || q.includes("where") || q.includes("look") || q.includes("help")) {
        triggerTaraWhereToLook();
      } else if (q.includes("story")) {
        sendTaraQuick("story");
      } else if (q.includes("clue") || q.includes("hint")) {
        sendTaraQuick("clue");
      } else {
        triggerTaraWhereToLook();
      }
    }

    // Auto-update Nexus Dashboard whenever stage changes or on load
    window.addEventListener("DOMContentLoaded", () => {
      setTimeout(updateNexusDashboard, 400);
    });

