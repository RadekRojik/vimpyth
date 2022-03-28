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

Script `pp.py` read the `.ccls` file from project if `gf` can't find file.
`pp.py` parse paths from `ccls` and in paths find file.

Add function in `init.vim`:

    function! MujPath(cohledam)                                                                                     
      " fce for better gf
      py3 sys.argv[1] = vim.eval('a:cohledam')
      py3file /home/radek/.config/nvim/myplug/pp.py
      return blabla
    endfunction
    " autocmd invoke gf
    autocmd BufRead *.cpp,+.hpp setlocal includeexpr=MujPath(v:fname)
