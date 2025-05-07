# 自动在 Raspberry Pi 上运行检测，并拉取图像结果
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
Write-Host "[$timestamp] Starting detection on Raspberry Pi..."

# 设置参数
$piUser = "ls25"
$piHost = "raspberrypi"
$remoteScriptPath = "/home/ls25/project/yolov5-mask-42-master/run_and_send.py"
$remoteBaseDir = "/home/ls25/project/yolov5-mask-42-master"
$targetFolder = "C:\Users\Liangcheng Sun\Desktop\445\bench organizor\code\detected_image"

# 运行 Raspberry Pi 上的 Python 脚本
ssh "$piUser@$piHost" "cd $remoteBaseDir && source ../env/bin/activate && python3 run_and_send.py"

# 等待几秒确保图片生成完成
Start-Sleep -Seconds 5

Write-Host "[$(Get-Date -Format "yyyy-MM-dd_HH-mm-ss")] Pulling detected images from Raspberry Pi..."

# 拉取 Raspberry Pi 上生成的检测图片
scp "$piUser@$piHost:$remoteBaseDir/autodetect_results_*/result_*/img_*.jpg" "$targetFolder"

Write-Host "[$(Get-Date -Format "yyyy-MM-dd_HH-mm-ss")]Done!"
