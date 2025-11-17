const readline = require("readline");
const fs = require("fs");
const simpleGit = require("simple-git");

const git = simpleGit(); // Initialize simple-git

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("How many commits do you want to make? ", async (answer) => {
  const count = parseInt(answer);

  if (isNaN(count) || count <= 0) {
    console.log("Invalid number. Exiting.");
    rl.close();
    return;
  }

  try {
    for (let i = 1; i <= count; i++) {
      // Modify dummy file (Git needs a file change)
      fs.writeFileSync("list.txt", `Commit ${i}: ${Date.now()}`);

      // Stage all files
      await git.add(".");

      // Commit
      await git.commit(`commit ${i}`);

      console.log(`✔ Commit ${i} done`);
    }

    
    // Push
    console.log("Pushing to GitHub...");
    await git.push("origin main", "HEAD");
1
    console.log("🚀 All commits pushed successfully!");
  } catch (err) {
    console.error("❌ Git error:", err);
  }

  rl.close();
});
