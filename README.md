# vimpyth
Littles helpers with my nvim

Script filename comments.py toogle only line basic commentsstrings.
Add this to `init.vim`

    function! Comment()                                                                                             
        " fce toogle comments
        py3file /home/radek/.config/nvim/myplug/comments.py
    endfunction

Invoke with:

    noremap <silent><C-c> :call Comment()<cr>
    inoremap <silent><C-c> <C-o>:call Comment()<cr>
