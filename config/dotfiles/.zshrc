########## OH MY ZSH ##########
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="robbyrussell"
plugins=(git)
source $ZSH/oh-my-zsh.sh


########## ALIASES ##########
# ls
alias ls="eza"
alias ll="eza -l"
alias la="eza -a"
alias lla="eza -l -a"
alias tree="eza -T"

# navigation
alias ..="cd .."
alias ~="cd ~"

# git
alias g="git"
alias gst="git status"
alias ga="git add"
alias gr="git reset"
alias gc="git commit"
alias gp="git push"
alias gl="git pull"
alias gra="git remote add"
alias gb="git branch"
alias gc="git checkout"

# clipboard management
alias clipb="pbcopy"


########## ZOXIDE ##########
eval "$(zoxide init zsh)"
