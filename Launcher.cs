using System;
using System.Diagnostics;
using System.IO;
using System.Windows.Forms;

namespace ProjectFailsafe
{
    static class Program
    {
        [STAThread]
        static void Main(string[] args)
        {
            try
            {
                string baseDir = AppDomain.CurrentDomain.BaseDirectory;
                string htmlPath = Path.Combine(baseDir, "public", "index.html");

                if (!File.Exists(htmlPath))
                {
                    MessageBox.Show(
                        "Could not locate 'public\\index.html'.\nPlease ensure ProjectFailsafe.exe is kept inside the project-failsafe folder.",
                        "PROJECT FAILSAFE - File Not Found",
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Error
                    );
                    return;
                }

                string fileUri = new Uri(htmlPath).AbsoluteUri;

                // Priority paths for Edge or Chrome
                string[] browserPaths = new string[]
                {
                    @"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                    @"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
                    @"C:\Program Files\Google\Chrome\Application\chrome.exe",
                    @"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                    Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), @"Microsoft\Edge\Application\msedge.exe"),
                    Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), @"Google\Chrome\Application\chrome.exe")
                };

                string chosenBrowser = null;
                foreach (string p in browserPaths)
                {
                    if (File.Exists(p))
                    {
                        chosenBrowser = p;
                        break;
                    }
                }

                if (chosenBrowser != null)
                {
                    ProcessStartInfo psi = new ProcessStartInfo();
                    psi.FileName = chosenBrowser;
                    // --app creates a dedicated native desktop window without browser toolbars, tabs, or address bar
                    psi.Arguments = string.Format("--app=\"{0}\" --window-size=1280,820", fileUri);
                    Process.Start(psi);
                }
                else
                {
                    // Fallback to default system browser
                    ProcessStartInfo psi = new ProcessStartInfo();
                    psi.FileName = fileUri;
                    psi.UseShellExecute = true;
                    Process.Start(psi);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error starting application: " + ex.Message, "PROJECT FAILSAFE Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
