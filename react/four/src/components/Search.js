import React from 'react'
import './Search.css'

class Search extends React.Component{
    state = {
        search: "",
        type: "all",
        page: 1
    }

    hanleKey = (event) => {
        if(event.key === 'Enter'){
            this.props.searchMovie(this.state.search, this.state.type, this.state.page)
        }
    }

    handleFilter = (event) => {
        this.setState(
            () => ({type: event.target.dataset.type}),
            () => {this.props.searchMovie(this.state.search, this.state.type, this.state.page)}
        )
    }

    nextPage = (event) => {
        this.setState(
            {page: this.state.page + 1},
            () => {this.props.searchMovie(this.state.search, this.state.type, this.state.page)}
        )
    }

    prevPage= (event) => {
        this.setState(
            this.state.page > 1 ? {page: this.state.page - 1} : {page: 1},
            () => {this.props.searchMovie(this.state.search, this.state.type, this.state.page)}
        )
    }

    render(){
        return(
            <>
                <div className="search">
                    <input 
                    type="search"
                    placeholder="Search"
                    value={this.state.search}
                    onChange={(e) => this.setState({search: e.target.value})}
                    onKeyDown={this.hanleKey}
                    />
                    <button
                        className='btn'
                        onClick={() => this.props.searchMovie(this.state.search, this.state.type, this.state.page)}
                    >Search</button>
                </div>
                <div className="radio">
                    <input type="radio" name="type" data-type="all" checked={this.state.type === 'all'} onChange={this.handleFilter} id='all' /> <label htmlFor="all">All</label>
                    <input type="radio" name="type" data-type="series" checked={this.state.type === 'series'} onChange={this.handleFilter} id='Series' /> <label htmlFor="Series">Series</label>
                    <input type="radio" name="type" data-type="movie" checked={this.state.type === 'movie'} onChange={this.handleFilter} id='Movies' /> <label htmlFor="Movies">Movies</label>
                    <input type="radio" name="type" data-type="game" checked={this.state.type === 'game'} onChange={this.handleFilter} id='Games' /> <label htmlFor="Games">Games</label>
                </div>
                <div className="navigation">
                    <button className='btn' onClick={this.prevPage}>Prev</button>
                    <button className='btn' onClick={this.nextPage}>Next</button>
                </div>
            </>
        )
    }
}

export default Search;