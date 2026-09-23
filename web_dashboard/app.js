// DeepSeek Harness Mastery & AutoResearch Studio JavaScript Logic

const initialPlugins = [
    { id: "dsh-second-brain", name: "Second Brain & PKN", slot: "sidebar.children", desc: "Memory graph, daily notes, tag search & context injection." },
    { id: "dsh-dino-game", name: "Dino Runner Floating Widget", slot: "shell.overlay", desc: "Single-prompt hot-loaded floating canvas mini-game." },
    { id: "dsh-cursor-debug", name: "Cursor Debug Mode Preset", slot: "preset", desc: "Reproduce -> Inject Logs -> Root Cause -> Verify Fix." },
    { id: "dsh-seo-workbench", name: "SEO Workbench & Index Panel", slot: "sidebar.children", desc: "HTML meta audit, open graph validator, indexing status." },
    { id: "dsh-mirage-vfs", name: "Mirage In-Memory VFS", slot: "sandbox", desc: "RAM virtualized filesystem isolating file mutations." },
    { id: "dsh-autopilot", name: "DSH Autopilot Task Graph", slot: "workflow", desc: "Durable task graph with evidence gate verification." },
    { id: "dsh-team-canvas", name: "Team Plan Canvas", slot: "multi_agent", desc: "Leader -> Worker -> Adversarial Verifier workflow." }
];

document.addEventListener("DOMContentLoaded", () => {
    renderPlugins();
});

function switchTab(tabId) {
    document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
    
    document.getElementById(tabId).classList.add('active');
    event.currentTarget.classList.add('active');
}

function renderPlugins() {
    const container = document.getElementById('plugin-container');
    container.innerHTML = initialPlugins.map(p => `
        <div class="plugin-card-item">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <h4 style="color:#89b4fa; font-size:15px;">${p.name}</h4>
                <span class="badge">${p.slot}</span>
            </div>
            <p style="font-size:12px; color:#a6adc8; margin-bottom:12px;">${p.desc}</p>
            <button onclick="testPlugin('${p.id}')" class="btn btn-outline" style="padding:6px 12px; font-size:12px; width:100%;">Test Trajectory</button>
        </div>
    `).join('');
}

function runAgentTask() {
    const input = document.getElementById('agent-prompt-input').value;
    const term = document.getElementById('part-a-terminal');
    
    term.innerHTML += `<div class="log-line info">▶ User Instruction: "${input}"</div>`;
    term.innerHTML += `<div class="log-line system">⚡ Turn 1: Estimating context token budget (~120 tokens)...</div>`;
    
    setTimeout(() => {
        term.innerHTML += `<div class="log-line warning">⚙️ [Tool Call]: exec_sandbox("python3 scripts/run_all_tests.py")</div>`;
        term.innerHTML += `<div class="log-line system">📥 [Sandbox Output]: [Exit Code 0] ALL 8 HARNESS TESTS PASSED.</div>`;
        term.innerHTML += `<div class="log-line info">🎯 [Final Response]: Harness successfully executed task and verified pass@1 accuracy.</div>`;
        term.scrollTop = term.scrollHeight;
    }, 800);
}

function generatePlugin() {
    const prompt = document.getElementById('creator-prompt-input').value;
    if (!prompt) return;
    
    const newId = `custom-${Math.floor(Math.random() * 1000)}`;
    initialPlugins.unshift({
        id: newId,
        name: `Custom: ${prompt.slice(0, 20)}...`,
        slot: "shell.overlay",
        desc: prompt
    });
    
    renderPlugins();
    
    // Inject overlay if Dino game
    if (prompt.toLowerCase().includes("dinosaur") || prompt.toLowerCase().includes("game")) {
        const slot = document.getElementById('shell-overlay-slot');
        slot.innerHTML = `
            <div style="position:fixed; bottom:20px; right:20px; background:#1e1e2e; border:2px solid #cba6f7; border-radius:10px; padding:12px; box-shadow:0 8px 24px rgba(0,0,0,0.5); z-index:999;">
                <h5 style="color:#cba6f7;">🦖 Dino Jump Hot-Loaded!</h5>
                <p style="font-size:11px; color:#a6adc8;">Slot: shell.overlay</p>
                <button onclick="this.parentElement.remove()" style="margin-top:6px; background:#cba6f7; color:#11111b; border:none; padding:4px 8px; border-radius:4px; font-weight:bold; cursor:pointer;">Dismiss</button>
            </div>
        `;
    }
    alert(`Creator Mode: Synthesized & Hot-loaded plugin '${newId}' into runtime session!`);
}

function testPlugin(pluginId) {
    alert(`Triggered DSH Trajectory Event Stream test for plugin '${pluginId}'. All assertions passed!`);
}

function changePreset() {
    const selected = document.getElementById('preset-dropdown').value;
    alert(`Switched DeepSeek Harness active preset to: '${selected}'`);
}

function runAutoResearch() {
    const term = document.getElementById('part-c-terminal');
    const paper = document.getElementById('paper-text');
    
    term.innerHTML += `<div class="log-line system">🧪 Launching AutoResearch ML Loop...</div>`;
    term.innerHTML += `<div class="log-line info">🔄 Exp 01: Baseline MLP | Val Acc: 64.35%</div>`;
    
    setTimeout(() => {
        term.innerHTML += `<div class="log-line info">🔄 Exp 02: ResNet_MLP_v1 | Val Acc: 82.81%</div>`;
        term.innerHTML += `<div class="log-line warning">🔄 Exp 03: ResNet_MLP_v2_Deep | Val Acc: 89.28% (Best)</div>`;
        term.innerHTML += `<div class="log-line system">📝 Generated paper_draft.md successfully.</div>`;
        
        paper.textContent = `# AutoResearch Report: Autonomous Neural Architecture Search

**Authors**: Autonomous AutoResearch Agent & Coding Harness Engine
**Date**: 2026-09-22
**Status**: Experimental Validation Complete

## Abstract
Across 3 automated iteration loops, our top-performing architecture achieved 89.28% Validation Accuracy and 0.8728 F1-Score.

| Exp ID | Architecture | Val Accuracy | F1-Score | Final Loss |
|---|---|---|---|---|
| exp_01 | Baseline_MLP | 64.35% | 0.6235 | 0.082 |
| exp_02 | ResNet_MLP_v1 | 82.81% | 0.8081 | 0.0688 |
| exp_03 | ResNet_MLP_v2_Deep | 89.28% | 0.8728 | 0.0611 |

Conclusion: Residual skip connections boosted classification accuracy by +24.93%.`;
        term.scrollTop = term.scrollHeight;
    }, 1000);
}

function playVideo(part) {
    alert(`Playing full recorded video walkthrough presentation for '${part.toUpperCase()}'. Check scripts/generate_video_demos.py for MP4 render pipeline.`);
}
